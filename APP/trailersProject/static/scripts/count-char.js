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

const categoryNameP = document.getElementById("category-name-p");
const categoryNameInput = document.getElementById("category-name-input");
categoryNameInput.addEventListener("input", (e)=>{
    let max = 50;
    let are = e.target.value.length;
    countChar(categoryNameP, max, are);
});

function countChar(p, max, are) {
    p.innerHTML = `(${are}/${max})`;
    if (are > max){
        p.classList.add("danger");
    }else{
        p.classList.remove("danger");
    }
}