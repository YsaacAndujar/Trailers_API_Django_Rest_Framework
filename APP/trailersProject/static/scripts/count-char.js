const titleP = document.getElementById("title-p");
const titleInput = document.getElementById("title-input");

titleInput.addEventListener("input", (e)=>{
    let max = 30;
    let are = e.target.value.length;
    titleP.value = `(${are}/${max})`;
});