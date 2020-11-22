const camera = document.querySelector("simple-camera");
let selectedField;
let imgResultModal = document.getElementById('img_result');

let setModalLabel = (label) => {
    let modalLabel = document.getElementById('camera_modal_label');
    modalLabel.innerText = label.replace('_', ' ');
}

let openCameraModal = async (option) => {
    setModalLabel(option.label);
    selectedField = document.getElementById(option.label);
    await camera.open({ video: { facingMode: "user" } });
};

let saveAndClose = async () => {
    selectedField.value = camera.takeBase64Photo({type: "jpeg", quality: 0.8}).base64;
    const view = document.getElementById(selectedField.name+'_result');
    view.removeAttribute('disabled');
    await camera.close()
    selectedField = undefined;
};

let openResult = (option) => {
    selectedField = document.getElementById(option.label);
    let blob = b64toBlob(selectedField.value);
    let url = URL.createObjectURL(blob);

    const imgTag = document.createElement('img');
    imgTag.src = url;
    imgTag.alt = option.label;

    imgResultModal.innerText = '';
    imgResultModal.append(imgTag);

};

let closeCameraModal = async () => {
    await camera.close();
};