//* Exercise 1

let h1 = document.getElementsByTagName("h1")[0];

function showBanner() {
    let banner = document.createElement("div");
    banner.textContent = "The sales ends in 10 mins!";
    banner.style.backgroundColor = "red";
    h1.appendChild(banner);
}

setTimeout(showBanner,5000);

//* Exercise 2

let counter = 10;
let div = document.createElement('div');
document.body.appendChild(div);
div.style.background = "red";


function banner() { 
    if (counter === 0) {
        clearInterval(id);
        return;
    }
    div.textContent = "The sales end in "+counter+" secs!";
    counter--;
  }

let id =setInterval(banner,1000);   

