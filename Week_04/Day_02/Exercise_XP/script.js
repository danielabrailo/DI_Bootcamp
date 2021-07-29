//Exercise 1

function infoAboutMe() {
    console.log("My name is Daniela and I love cats!!!");
}
infoAboutMe();

function infoAboutPerson(personName, personAge, personFavoriteColor, personHobbies) {
    console.log("Your name is "+ personName + ", you are " + personAge+ " years old, your favorite color is "+ personFavoriteColor+ " and your hobbies are: ");
    for (hobbie in personHobbies) {
        console.log(personHobbies[hobbie]);
    }
}

infoAboutPerson("David", 45, "blue", ["tennis", "painting"])
infoAboutPerson("Josh", 12, "yellow", ["videoGame", "hanging out with friends", "playing cards"])


//Exercise 2
function checkDriverAge(age) {
    if (age < 18) {
        alert("Sorry, you are too young to drive this car. Powering off");
    }
    else if (age > 18) {
        alert("You are old enough to drive, Powering On. Enjoy the ride!");
    }
    else if (age === 18) {
        alert("Congratulations on your first year of driving. Enjoy the ride!");
    }
}

checkDriverAge(18);

//Exercise 3
function checkNumber() {
    for (i=0; i<101; i++) {
        if (i%2 ===0) {
            console.log("The number " + i+ " is even");
        }
        else {
            console.log("The number " + i+ " is odd");
        }
    }
}
checkNumber();

//Exercise 4
function isDivisible(divisor) {
    let sum=0;
    for (i=0; i<501; i++) {
        if (i%divisor === 0) {
            console.log(i);
            sum += i;
        }
    }
    console.log("sum: "+sum);
}
isDivisible(23);

//Exercise 5
let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}

function checkBasket(){
    let item = prompt("Choose an item");
    if (item in amazonBasket) {
        alert("The item is in the basket");
    }
    else {
        alert("The item is not available");
    }
}

checkBasket();

//Exercise 6
function changeEnough([quarters, dimes, nickels, pennies], price) {
    let sum = (quarters*0.25) + (dimes*0.1) + (nickels*0.05) + (pennies*0.01);
    if (sum >= price) {
        console.log("true");
    }
    else {
        console.log("false");
    }
}

changeEnough([2, 100, 0, 0], 14.11);
changeEnough([0, 0, 20, 5], 0.75);

//Exercise 7
let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

let shoppingList = ["banana", "orange", "apple"];
function myBill() {
    let sum=0;
    for (let i=0; i<shoppingList.length; i++){
      if (shoppingList[i] in stock && stock[shoppingList[i]] > 0){ // Checking if item is in stock        
        sum += prices[shoppingList[i]];     
       }
}
console.log(sum); // the final price of the shopping list
}

myBill();

//Exercise 8
function tipCalculator() {
    let bill = prompt("How much was the bill?");
    let tip;
    if (bill < 50) {
        tip = parseInt((bill * 0.2));
        console.log("The tip should be: $" + tip);
    }
    else if (bill <= 200) {
        tip = parseInt((bill * 0.15));
        console.log("The tip should be: $" + tip);
    }
    else if (bill > 200) {
        tip = parseInt((bill * 0.1));
        console.log("The tip should be: $" + tip);
    }    
    console.log("The final bill is: $" + (+bill + tip));
}

tipCalculator();

//Exercise 9
function hotelCost() {
    let nights = prompt("How many nights are you staying at the hotel?");
    if (!nights || isNaN(nights)) {
        hotelCost();
    }
    else {
        return (+nights * 140);       
    }
    
}

function planetRideCost() {
    let destination = prompt("What is your destination?");
    if (!destination) {
        planetRideCost();
    }
    else if (destination === "London") {
        return 183;    
    }
    else if (destination === "Paris") {
        return 220;
    }
    else {
        return 300;
    }
    }

  function rentalCarCost() {
      let days = prompt("How many days are you renting the car?");
      if (!days || isNaN(days)) {
          rentalCarCost();
      }
      let totalCost = (+days * 40);
      if (days >= 10) {
          totalCost = (totalCost - (totalCost*0.05));
      }
      return totalCost; 
      }
    
function totalVacationCost() {
    console.log(parseInt(hotelCost() + planetRideCost() + rentalCarCost()));
}

totalVacationCost();