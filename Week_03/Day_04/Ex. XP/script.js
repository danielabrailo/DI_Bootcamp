// Exercise 1
var x = 8;
var y = 5;

if (x>y) {
    console.log("X is the biggest number");
}

else if (x<y) {
    console.log("Y is the biggest number");
}

// Exercise 2
var newDog = "Chihuahua";
console.log(newDog.length);
console.log(newDog.toUpperCase());
console.log(newDog.toLowerCase());

if (newDog === "Chihuahua") {
    console.log("I love Chihuahuas, it’s my favorite dog breed");
}
else {
    console.log("I dont care, I prefer cats");
}

// Exercise 3
var num = prompt("Enter a number", 10);
if (num%2 === 0) {
    alert(num + " is an even number!");
}
else {
    alert(num + " is an odd number!");
}

// Exercise 4
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]

switch (users.length) {
    case 0:
        console.log("No one is online");
        break;
    case 1:
        console.log(users + " is online");
        break;
    case 2:
        console.log(users[0] + " and " + users[1] + " are online");
        break;
    default:
        if (users.length>2)
        console.log(users[0] + ", " + users[1] +" and " + (users.length-2) + " more are online");
}