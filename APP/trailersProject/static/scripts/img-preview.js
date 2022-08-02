const imageUpload = document.getElementById("imageUpload")
const imagePreview = document.getElementById("imagePreview");
imageUpload.onchange = evt => {
    const [file] = imageUpload.files;
    if (file) {
        imagePreview.src = URL.createObjectURL(file);
        imagePreview.classList.remove("hide");
    }
}