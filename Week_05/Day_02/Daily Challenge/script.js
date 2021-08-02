//Getting the values of all the inputs and elements
let noun = document.getElementById("noun");
let adj = document.getElementById("adjective");
let person = document.getElementById("person");
let verb = document.getElementById("verb");
let place = document.getElementById("place");
let btn = document.getElementById("lib-button");
let story = document.getElementById("story");
// let shuffle = document.createElement("button");

btn.addEventListener("click", createStory);

//Creating story
function createStory() {
    if (checkEmpty() === true)
    return;
    else {
        let generatedStory = document.createTextNode("Once upon a time there was a person named " +person.value+ " who loved going to the " +place.value+ " to " +verb.value+ " with a very " +adj.value+ " " +noun.value);
        story.appendChild(generatedStory);
    }
}

// Checking if the in puts are empty
function checkEmpty() {
    if (noun.value.length === 0) {
        alert("You forgot to add a noun!");
        return true;
    }
    if (adj.value.length === 0) {
        alert("You forgot to add an adjective!");
        return true;
    }
    if (person.value.length === 0) {
        alert("You forgot to add a person!");
        return true;
    }
    if (verb.value.length === 0) {
        alert("You forgot to add a verb!");
        return true;
    }
    if (place.value.length === 0) {
        alert("You forgot to add a place!");
        return true;
    }
}