//*Exercise 1

function insertRow() {
    let table = document.getElementById('sampleTable');

    //First create the rows
    let TableRow = document.createElement('tr');

    //Create the 2 cells of the row
    let cel0 = TableRow.insertCell(0)
    let cel1 = TableRow.insertCell(1)

    cel0.textContent = "cel0";
    cel1.textContent = "cel1";

    //Add the rows to the table
    table.appendChild(TableRow);

}

//* Exercise 2 - Event Listeners
let x = document.getElementById("jsstyle");

x.addEventListener("mouseover", changeBackground);
x.addEventListener("click", changeColor);

function changeBackground() {
    x.style.backgroundColor = "red";
}

function changeColor() {
    x.style.color = "white";
}

//* Exercise 3 - Propagation
let x = document.getElementById("jsstyle");
let y = document.getElementById("div");

x.addEventListener("click", changeBackground);
y.addEventListener("click", changeYBackground);

function changeBackground(e) {
    x.style.backgroundColor = "red";
    e.stopPropagation();
}

function changeYBackground() {
    y.style.backgroundColor = "blue";
}

//* Exercise 4 - Forms
function getvalue() {

    let form = document.getElementById("form1");
    let firstName = form.elements.fname.value;
    let lastName = form.elements.lname.value;
    
    alert("the full name is "+firstName+ " " +lastName);
}

//* Exercise 5 - Select
let dropdown = document.getElementById("select1");

// Question 1
// console.log(dropdown[1].value);
// alert(dropdown.options[1].textContent);

// Question 2
let newOption = document.createElement("option");
newOption.value = "Work";
newOption.textContent = "Work";
dropdown.appendChild(newOption);

// Question 3
let newOption2 = document.createElement("option");
newOption2.value = "Primary School";
newOption2.textContent = "Primary School";
dropdown.add(newOption2, 0); 

// Question 4
dropdown.options[3].selected = true;

// Question 5
let showSelectedBtn = document.getElementById("showSelected");
showSelectedBtn.onclick = function() {
    alert(dropdown.selectedOptions[0].textContent); }