
// (async function() {
//         const camera = document.querySelector("simple-camera");
//         const btnBase64Photo = document.querySelector("#btnBase64Photo");
//         await camera.open({ video: { facingMode: "user" } });
//         btnBase64Photo.addEventListener("click", async event => {
//             const photo = camera.takeBase64Photo({ type: "jpeg", quality: 0.8 });
//             console.log(photo);
//         });
// })();