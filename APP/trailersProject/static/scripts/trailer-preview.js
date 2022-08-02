const frame= document.getElementById("frame");
const code = document.getElementById("code");
code.addEventListener("input",(e)=>{
    changeUrl(e.target.value);
});

function changeUrl(code) {
    let url = "https://www.youtube.com/embed/"+code
    frame.src=url;
}