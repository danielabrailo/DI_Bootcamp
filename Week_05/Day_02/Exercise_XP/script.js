// Exercise 1 - Question 1
let lastParagraph = document.getElementsByTagName("article")[0].lastElementChild;
lastParagraph.remove();

// Question 2
let h2 = document.getElementsByTagName("h2")[0];

h2.addEventListener("click", function () {
    h2.style.backgroundColor = "red";
})

// Question 3
let h1 = document.getElementsByTagName("h1")[0];

h1.style.fontSize = (Math.floor(Math.random() * 101)) + "px";

// Question 4
let h3 = document.getElementsByTagName("h3")[0];
h3.addEventListener("click", function() {
    h3.style.display = "none";
})

// Question 5
let btn = document.createElement("button");
let paragraphs = document.getElementsByTagName("p");
btn.textContent = "Change font style";
h1.appendChild(btn);
btn.addEventListener("click", function() {
    for (i=0; i<paragraphs.length; i++){   
    paragraphs[i].style.fontWeight = "bold";
    }
})

//Question 6
let form = document.forms;
let submitBtn = document.getElementById("submit");
let fname = document.getElementById("fname");
let lname = document.getElementById("lname");
let userAnswer = document.getElementsByClassName("usersAnswer");

submitBtn.addEventListener("click", getValues);

function getValues(e) {
    if (checkIfEmpty() === true)
    return;
    else {
        let userInput = document.createTextNode("Your answer is: " + fname.value+ " "+ lname.value);
        userAnswer[0].appendChild(userInput);
        e.preventDefault();
    }
}

function checkIfEmpty() {
    if (fname.value.length === 0) {
        alert("You forgot to write your first name!");
        return true;
    }
    if (lname.value.length === 0) {
        alert("You forgot to write your last name!");
        return true;
} 
}

// Question 7
let secondParagraph = document.getElementsByTagName("p")[1];

secondParagraph.addEventListener("mouseover", fade);

function fade() {
    secondParagraph.style.opacity = "0.1";
}

// Exercise 2 
let boldItems = document.getElementsByTagName("strong");    

function highlight() {
    for (i=0; i<boldItems.length;i++){
        boldItems[i].style.backgroundColor = "blue";
    }
}

function return_normal() {
    for (i=0; i<boldItems.length;i++){
        boldItems[i].style.backgroundColor = "white";
    }
}

let paragraph = document.getElementsByTagName("p")[0];

paragraph.addEventListener("mouseover", highlight);
paragraph.addEventListener("mouseout", return_normal);

//Exercise 3 - Program to calculate the volume of a sphere
let radius = document.getElementById("radius");
let btn = document.getElementById("submit");

btn.addEventListener("click", getVolume);

function getVolume(e){
    e.preventDefault();
    let volume = (4/3)* Math.PI * Math.pow(radius.value,3);
    volume = volume.toFixed(3);
    alert("The volume of the sphere is: " + volume);
}

// Exercise 4
let test = document.getElementById("test");

test.addEventListener("click", function() {
    test.style.backgroundColor = "yellow";
})

test.addEventListener("copy", function() {
    alert("Element copied!");
})

test.addEventListener("dblclick", function() {
    test.style.fontSize = 30+"px";})


test.addEventListener("mouseover", function(){
    test.style.backgroundColor = "pink";
})

test.addEventListener("mouseout", function(){
    test.style.backgroundColor = "white";
})