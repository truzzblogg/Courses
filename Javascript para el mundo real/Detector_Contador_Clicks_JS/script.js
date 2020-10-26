// Udemy course: Javascript para el mundo real!
// https://www.udemy.com/course/javascript-para-el-mundo-real/

let counter = 0;
let message = "Hey! STOP! You have clicked so many times!"
function countingClicks() {
  document.getElementById("counting").innerHTML = ++counter;
  if(counter > 10){
    document.getElementById("warning").innerHTML = message;
  }
  
}