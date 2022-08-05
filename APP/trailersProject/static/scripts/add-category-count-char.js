const categoryNameP = document.getElementById("category-name-p");
const categoryNameInput = document.getElementById("category-name-input");
categoryNameInput.addEventListener("input", (e)=>{
    let max = 50;
    let are = e.target.value.length;
    countChar(categoryNameP, max, are);
});
countChar(categoryNameP, 50, categoryNameInput.value.length);