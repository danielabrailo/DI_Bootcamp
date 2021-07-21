// Exercise 1
var language = prompt("What language do you speak?", "English");

language = language.toLowerCase();

switch (language) {
    case "french":
        alert("Bonjour!");
        break;
    case "english":
        alert("Hello!");
        break;
    case "hebrew":
        alert("Shalom!");
        break;
    case "chinese":
        alert("Ni hao!");
        break;
    default:
        alert("01110011 01101111 01110010 01110010 01111001");
}

// Exercise 2
var grade = prompt("What is your grade?", 100);

switch (true) {
    case (grade < 70): 
        console.log("D");
        break;
    case (grade <= 80):
        console.log("C");
        break;
    case (grade <= 90):
        console.log("B");
        break;
    case (grade > 90):
        console.log("A");
        break;
    default:
        console.log("Please enter a valid grade");
}

// Exercise 3
var verb = prompt("Enter a verb", "go");

if (verb.length >= 3 && !verb.endsWith("ing")) {
    console.log(verb+"ing");
}

else if (verb.length >= 3 && verb.endsWith("ing")) {
    console.log(verb+"ly");
}

else if (verb.length < 3) {
    console.log(verb);
}