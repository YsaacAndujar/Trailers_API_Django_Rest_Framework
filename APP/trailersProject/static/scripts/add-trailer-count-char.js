const titleP = document.getElementById("title-p");
const titleInput = document.getElementById("title-input");
titleInput.addEventListener("input", (e)=>{
    let max = 70;
    let are = e.target.value.length;
    countChar(titleP, max, are);
});

const castP = document.getElementById("cast-p");
const castInput = document.getElementById("cast-input");
castInput.addEventListener("input", (e)=>{
    let max = 100;
    let are = e.target.value.length;
    countChar(castP, max, are);
});

const descriptionP = document.getElementById("description-p");
const descriptionInput = document.getElementById("description-input");
descriptionInput.addEventListener("input", (e)=>{
    let max = 200;
    let are = e.target.value.length;
    countChar(descriptionP, max, are);
});

const codeP = document.getElementById("code-p");
const codeInput = document.getElementById("code");
codeInput.addEventListener("input", (e)=>{
    let max = 15;
    let are = e.target.value.length;
    countChar(codeP, max, are);
});

