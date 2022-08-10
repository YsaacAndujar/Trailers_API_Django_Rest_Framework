const oldPasswordP = document.getElementById("old-password-p");
const oldPasswordInput = document.getElementById("old-password-input");
oldPasswordInput.addEventListener("input", (e)=>{
    let max = 150;
    let are = e.target.value.length;
    countChar(oldPasswordP, max, are);
});
countChar(oldPasswordP, 150, oldPasswordInput.value.length);

const newPasswordP = document.getElementById("new-password-p");
const newPasswordInput = document.getElementById("new-password-input");
newPasswordInput.addEventListener("input", (e)=>{
    let max = 150;
    let are = e.target.value.length;
    countChar(newPasswordP, max, are);
});
countChar(newPasswordP, 150, newPasswordInput.value.length);


