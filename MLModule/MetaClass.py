from abc import abstractmethod


class Recognize:
    recognizer = None
    detector = None
    dataset_path = None
    trainer_path = None

    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def generate_training_model(self):
        pass

    @abstractmethod
    def recognize(self):
        pass
