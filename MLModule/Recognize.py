from abc import ABC

import cv2
import numpy as np
import os
from PIL import Image
import base64
from python_speech_features import mfcc
import librosa
from hmmlearn import hmm
import pickle
from sklearn import preprocessing
from sklearn import mixture
from scipy.io.wavfile import read

import MLModule.MetaClass as Meta


def calculate_delta(array):
    """Calculate and returns the delta of given feature vector matrix"""

    rows, cols = array.shape
    deltas = np.zeros((rows, 20))
    N = 2
    for i in range(rows):
        index = []
        j = 1
        while j <= N:
            if i - j < 0:
                first = 0
            else:
                first = i - j
            if i + j > rows - 1:
                second = rows - 1
            else:
                second = i + j
            index.append((second, first))
            j += 1
        deltas[i] = (array[index[0][0]] - array[index[0][1]] + (2 * (array[index[1][0]] - array[index[1][1]]))) / 10
    return deltas


def extract_features(audio, rate):
    """extract 20 dim mfcc features from an audio, performs CMS and combines
    delta to make it 40 dim feature vector"""

    mfcc_feat = mfcc(audio, rate, 0.025, 0.01, 20, appendEnergy=True)
    mfcc_feat = preprocessing.scale(mfcc_feat)
    delta = calculate_delta(mfcc_feat)
    combined = np.hstack((mfcc_feat, delta))
    return combined


def convert_and_save(b64_string, path):
    b64_string = b64_string.partition('base64,')[2]
    with open(path, "wb") as fh:
        fh.write(base64.b64decode(b64_string.encode()))


class Face(Meta.Recognize):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier("MLModule/classifiers/face.xml")
    dataset_path = None
    trainer_path = 'trainer/face.yml'

    def train(self, img_path=None):
        image_paths = [os.path.join(img_path, f) for f in os.listdir(img_path)]
        face_samples = []
        face_ids = []
        for imagePath in image_paths:

            if os.path.split(imagePath)[-1].split(".")[-1] != 'jpeg':
                continue

            pil_image = Image.open(imagePath).convert('L')
            image_np = np.array(pil_image, 'uint8')
            face_id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = self.detector.detectMultiScale(image_np)
            for (x, y, w, h) in faces:
                face_samples.append(image_np[y:y + h, x:x + w])
                face_ids.append(face_id)
        return face_samples, face_ids

    def generate_training_model(self, dataset_path=None):
        faces, face_ids = self.train(dataset_path)
        self.recognizer.train(faces, np.array(face_ids))
        self.recognizer.save(self.trainer_path)

    def recognize(self, img_path=None):
        im = cv2.imread(img_path)
        print(img_path)
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(self.trainer_path)
        face_cascade = self.detector

        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(im, 1.2, 5)

        if len(faces) != 0:
            for (x, y, w, h) in faces:
                face_id, conf = recognizer.predict(gray[y:y + h, x:x + w])
                if conf < 50:
                    return face_id, conf
                else:
                    return None, None
        else:
            return None, None


class Speech(Meta.Recognize):
    dataset_path = None
    trainer_path = 'trainer/face.yml'
    dataset = None

    def __init__(self, dataset_path=None):
        self.dataset_path = dataset_path

    def train(self):

        file_list = [f for f in os.listdir(self.dataset_path) if os.path.splitext(f)[1] == '.wav']

        for file in file_list:
            sr, audio = read(self.dataset_path + file)
            vector = extract_features(audio, sr)

            gmm = mixture.GaussianMixture(n_components=16, covariance_type='diag', n_init=3)
            gmm.fit(vector)
            pickle.dump(gmm, open('training_data/' + file.split('.')[1] + ".gmm", 'wb'))

    def generate_training_model(self):
        self.train()

    def recognize(self, test_file_path=None):

        print(test_file_path)
        gmm_files = [f for f in os.listdir('training_data') if os.path.splitext(f)[1] == '.gmm']
        models = [pickle.load(open('training_data/' + file_name, 'rb')) for file_name in gmm_files]

        sr, audio = read(test_file_path)
        vector = extract_features(audio, sr)
        log_likelihood = np.zeros(len(models))

        for i in range(len(models)):
            gmm = models[i]
            scores = np.array(gmm.score(vector))
            log_likelihood[i] = scores.sum()

        winner = np.argmax(log_likelihood)
        print(gmm_files[winner].split('.')[0], log_likelihood[winner])
        return gmm_files[winner].split('.')[0], log_likelihood[winner]

