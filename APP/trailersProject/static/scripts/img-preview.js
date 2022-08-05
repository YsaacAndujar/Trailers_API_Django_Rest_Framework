const imageUpload = document.getElementById("imageUpload");
const imagePreview = document.getElementById("imagePreview");
imageUpload.onchange = evt => {
    loadImgPreview();
}
function loadImgPreview(){
    const [file] = imageUpload.files;
    if (file) {
        imagePreview.src = URL.createObjectURL(file);
        imagePreview.classList.remove("hide");
    }
}