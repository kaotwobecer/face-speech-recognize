let startRecordButton = document.getElementById('speech_path_start');
let stopRecordButton = document.getElementById('speech_path_stop');
let resultFile = document.getElementById('speech_path_file');
let speechInput = document.getElementById('speech_path');
const reader = new FileReader();

let audioTrack = new WebAudioTrack(null);

startRecordButton.onclick = e => {

    audioTrack.startRecording(() => {
        setButtonStartRecording();
    });
}

stopRecordButton.onclick = e => {
    audioTrack.stopRecording(() => {

        if (!audioTrack.isCaptureInProgress) {
            setButtonStopRecording();
            showResult();

            reader.readAsDataURL(audioTrack.blob);
            reader.addEventListener('loadend', () => {
                speechInput.value = reader.result;
            })
        }


    });
}

let showResult = () => {
    resultFile.innerHTML = '';

    const playButton = document.createElement('div');
    playButton.innerText = 'Play';
    playButton.setAttribute('class', 'btn btn-info');
    playButton.addEventListener('click', () => {
        audioTrack.play();
    });

    resultFile.append(playButton);


};

let setButtonStartRecording = () => {
    startRecordButton.setAttribute('disabled', 'true');
    startRecordButton.setAttribute('class', 'btn btn-light');

    stopRecordButton.removeAttribute('disabled');
    stopRecordButton.setAttribute('class', 'btn btn-danger');
}

let setButtonStopRecording = () => {
    startRecordButton.removeAttribute('disabled');
    startRecordButton.setAttribute('class', 'btn btn-success');

    stopRecordButton.setAttribute('disabled', 'true');
    stopRecordButton.setAttribute('class', 'btn btn-light');
}