const accountUsernameP = document.getElementById("account-username-p");
const accountUsernameInput = document.getElementById("account-username-input");
accountUsernameInput.addEventListener("input", (e)=>{
    let max = 150;
    let are = e.target.value.length;
    countChar(accountUsernameP, max, are);
});
countChar(accountUsernameP, 150, accountUsernameInput.value.length);

const accountEmailP = document.getElementById("account-email-p");
const accountEmailInput = document.getElementById("account-email-input");
accountEmailInput.addEventListener("input", (e)=>{
    let max = 150;
    let are = e.target.value.length;
    countChar(accountEmailP, max, are);
});
countChar(accountEmailP, 150, accountEmailInput.value.length);

const accountFirst_nameP = document.getElementById("account-first_name-p");
const accountFirst_nameInput = document.getElementById("account-first_name-input");
accountFirst_nameInput.addEventListener("input", (e)=>{
    let max = 150;
    let are = e.target.value.length;
    countChar(accountFirst_nameP, max, are);
});
countChar(accountFirst_nameP, 150, accountFirst_nameInput.value.length);

const accountLast_nameP = document.getElementById("account-last_name-p");
const accountLast_nameInput = document.getElementById("account-last_name-input");
accountLast_nameInput.addEventListener("input", (e)=>{
    let max = 150;
    let are = e.target.value.length;
    countChar(accountLast_nameP, max, are);
});
countChar(accountLast_nameP, 150, accountLast_nameInput.value.length);

