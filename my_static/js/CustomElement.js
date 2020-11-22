class SimpleCamera extends HTMLElement {

    open(constraints) {
        return navigator.mediaDevices.getUserMedia(constraints)
            .then((mediaStream) => {
                // Assign the MediaStream!
                this.videoElement.srcObject = mediaStream;
                // Play the stream when loaded!
                this.videoElement.onloadedmetadata = (e) => {
                    this.videoElement.play();
                };
            });
    }

    close() {
        this.videoElement.srcObject.getTracks().forEach(track => track.stop());
    }

    connectedCallback() {
        const shadow = this.attachShadow({mode: "open"});
        this.videoElement = document.createElement("video");
        this.canvasElement = document.createElement("canvas");
        this.videoElement.setAttribute("playsinline", true);
        this.canvasElement.style.display = "none";
        this.videoElement.style.transform = "scaleX(-1)";
        this.videoElement.style.width = "100%";
        shadow.appendChild(this.videoElement);
        shadow.appendChild(this.canvasElement);
    }

    _drawImage() {
        const imageWidth = this.videoElement.videoWidth;
        const imageHeight = this.videoElement.videoHeight;

        const context = this.canvasElement.getContext('2d');
        this.canvasElement.width = imageWidth;
        this.canvasElement.height = imageHeight;

        context.drawImage(this.videoElement, 0, 0, imageWidth, imageHeight);

        return {imageHeight, imageWidth};
    }

    takeBase64Photo({type, quality} = {type: 'png', quality: 1}) {
        const {imageHeight, imageWidth} = this._drawImage();
        const base64 = this.canvasElement.toDataURL('image/' + type, quality);
        return {base64, imageHeight, imageWidth};
    }

}


customElements.define("simple-camera", SimpleCamera);
