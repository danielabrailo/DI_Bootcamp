//      Exercise 1
console.log("Exercise 1");
let colors = ["red", "blue", "pink", "purple"];

let suff = ["1st","2nd","3rd","4th"];

for (let i=0; i<colors.length; i++){
    console.log("My "+ suff[i]+ " choice is "+ colors[i]);
}

//     //   Exercise 2
console.log("Exercise 2");
let people = ["Greg", "Mary", "Devon", "James"];
people.shift();
people[2] = "Jason";
people.push("Daniela");

for (person in people) {
    console.log(people[person]);
}

for (person in people) {
    if (people[person] === "Daniela") {
        break;
    }
    console.log(people[person]);
}

let copyPeople = people.slice(1);
console.log(people);
console.log(copyPeople);

console.log(people.indexOf("Mary"));
console.log(people.indexOf("Foo"));

let last = people[(people.length)-1];
console.log(last);


// // Exercise 3
do {
    var num = prompt("Choose a number higher than 10", 15);
} while (num < 10);

// // Exercise 4
console.log("Exercise 4");
let guestList = {
    randy: "Germany",
    karla: "France",
    wendy: "Japan",
    norman: "Ëngland",
    sam: "Argentina"
}

let name = prompt("What is your name?", "randy");

if (name in guestList) {
    console.log("Hi I'm " +name+ " and I'm from " + guestList[name]);
}
else {
    console.log("Hi! I'm a guest");
}

// Exercise 5
console.log("Exercise 5");
let family = {
    Mother: "Monica",
    Father: "John",
    Brother: "Jack"
}
for (let key in family) {
    console.log(key);
}

for (let value in family) {
    console.log(family[value]);
}

// Exercise 6
console.log("Exercise 6");
let details = {
    my: "name",
    is: "Rudolf",
    the: "raindeer"
}

var result = [];
for (key in details) {
    result = result + (key + " " + details[key] + " ");
}
console.log(result);

// Exercise 7
console.log("Exercise 7");
let names = ["Jack","Philip","Sarah","Amanda","Bernard","Kyle"];
var society = [];
for (let i=0; i<names.length; i++) {
    society = society + names[i][0];
}
console.log("The name of the secret society is: " + society);