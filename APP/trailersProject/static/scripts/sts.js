const from = document.getElementById("from-sts");
const to = document.getElementById("to-sts");
const add = document.getElementById("add-sts");
const remove = document.getElementById("remove-sts");

add.addEventListener("click",()=>{
    moveSts(from, to);
});

remove.addEventListener("click",()=>{
    moveSts(to, from);
});

function moveSts(fm, t) {
    if(fm.length <= 0){
        return;
    }
    option = fm.options[fm.selectedIndex];
    t.add(option);
}