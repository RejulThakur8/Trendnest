document.getElementById("details").style.width = "500px";

const subtract = document.querySelector(".subtraction"),
 number = document.querySelector(".num"),
 add = document.querySelector(".addition");

let a = 1;

subtract.addEventListener('click', ()=>{
    if(a > 1){
        a--;
        a = (a < 10) ? + a : a;
        number.innerHTML = a;
    }
});

add.addEventListener('click', ()=>{
    a++;
    a = (a < 10) ?  + a : a;
    number.innerHTML = a;
});