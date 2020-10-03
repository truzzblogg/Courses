

// function btnChanger() {
//     let bg = document.getElementById("container").style.background = "red";
//     let x = document.getElementById("btn-color").style.background = "indigo";
//     let y = document.getElementById("btn-color").style.color = "gold";
    
// }

// let colors = ["tomato", "grey", "red", "violet", "purple", "blue", "teal", "gold"];
// let colors2 = ["white", "orange", "indigo", "pink", "lightcoral", "black", "cyan"];

// function btnChanger() {
//         let random = Math.floor(Math.random() * colors.length);
//         let random2 = Math.floor(Math.random() * colors2.length);
//         console.log("Random value: " + random);
//         console.log("Random2 value: " + random2);
//         let x = document.getElementById("btn-color").style.background = colors[random];
//         let y = document.getElementById("btn-color").style.color = colors2[random2];
//         let z = document.getElementById("container").style.background = colors2[random2];
    
   

// }

function btnChanger(){
    let x_bg = Math.floor(Math.random() * 256);
    let y_bg = Math.floor(Math.random() * 256);
    let z_bg = Math.floor(Math.random() * 256);
    let x_btnColor = Math.floor(Math.random() * 256);
    let y_btnColor = Math.floor(Math.random() * 256);
    let z_btnColor = Math.floor(Math.random() * 256);
    

    // bgColor = "rgb(" + x_bg + "," + y_bg + "," + z_bg + ")";
    bgColor = `rgb(${x_bg}, ${y_bg}, ${z_bg})`;
    console.log(bgColor);
    btnColor = "rgb(" + x_btnColor + "," + y_btnColor + "," + z_btnColor + ")";
    console.log(btnColor);

    let btn_change_bg = document.querySelector('.changeBG');
    let changeBG = btn_change_bg.style.background = bgColor;

    let x = document.getElementById("btn-color").style.background = btnColor;

    let btn_text_colors = ["black", "white"];
    let random = Math.floor(Math.random() * btn_text_colors.length);
    let y = document.getElementById("btn-color").style.color = btn_text_colors[random];

}



