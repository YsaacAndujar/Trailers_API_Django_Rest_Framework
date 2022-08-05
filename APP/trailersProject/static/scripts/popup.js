const closeConfirmation = document.getElementById("close-confirmation-popup");
const openConfirmation = document.getElementById("open-confirmation-popup");
const confirmation = document.getElementById("confirmation-popup");
closeConfirmation.addEventListener("click",()=>{
    togglePopup(confirmation);
});
openConfirmation.addEventListener("click",()=>{
    togglePopup(confirmation);
});
try {
    const closeDelete = document.getElementById("close-delete-popup");
    const openDelete = document.getElementById("open-delete-popup");
    const deletePopup = document.getElementById("delete-popup");
    closeDelete.addEventListener("click",()=>{
        togglePopup(deletePopup);
    });
    openDelete.addEventListener("click",()=>{
        togglePopup(deletePopup);
    });  
} catch (error) {
    
}


const ok = document.getElementById("ok-popup");
const closeOk = document.getElementById("close-ok-popup");
closeOk.addEventListener("click",()=>{
    togglePopup(ok);
});

const error = document.getElementById("error-popup");
const closeError = document.getElementById("close-error-popup");
closeError.addEventListener("click",()=>{
    togglePopup(error);
});

function togglePopup(popup) {
    popup.classList.toggle("active");
}
