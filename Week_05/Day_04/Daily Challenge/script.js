let listTasks = [];
let btn = document.getElementById("submitBtn");
let newTask = document.getElementById("task");
let showTasks = document.getElementsByClassName("listTasks");

btn.addEventListener("click", addTask);

function addTask(e) {
    e.preventDefault();

    if (checkEmpty() === true)
        return;
    else{
        //Adding the X button
        let xBtn = document.createElement("button");
        xBtn.className = "fas fa-times";
        showTasks[0].appendChild(xBtn);

        //Adding the checkbox
        let newCheckbox = document.createElement("input");
        newCheckbox.type = "checkbox";
        newCheckbox.id = "checkbox";
        showTasks[0].appendChild(newCheckbox);

        //Adding the new item to the list
        let nodeTask = document.createTextNode(newTask.value);              
        listTasks.push(nodeTask);  
        showTasks[0].appendChild(nodeTask);
        let space = document.createElement("br");
        showTasks[0].appendChild(space); 
             
    }
    
}

// Checking that the input is not empty
function checkEmpty() {
    if (newTask.value.length === 0){
        alert("You forgot to add a new task!")
        return true;
    }
}