let color_boxes = document.querySelectorAll(".colors > *");
let blank_boxes = document.querySelectorAll(".squares > *");
let clear_btn = document.getElementsByTagName("button")[0];
let body = document.getElementsByTagName("body")[0];

let color = null;
let mousedown = false;

body.addEventListener("mousedown", function() {
    mousedown = true;
})

body.addEventListener("mouseup", function() {
    mousedown = false;
})

// Choosing a color
for (color_box of color_boxes) {
    color_box.addEventListener("click", function(event) {
        color = event.target.style.backgroundColor;
    })
}

// Coloring
for (blank_box of blank_boxes) {
    blank_box.addEventListener("mousedown", function(event) { 
        if (color != null) event.target.style.backgroundColor = color;
    })
    blank_box.addEventListener("mouseover", function(event) {
        if (mousedown && color != null) event.target.style.backgroundColor = color;
    })
}

// Clearing all the colors
clear_btn.addEventListener("click", function() {
    for (blank_box of blank_boxes) {
        blank_box.style.backgroundColor = "white";
    }
})