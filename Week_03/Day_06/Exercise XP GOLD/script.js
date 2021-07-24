//Exercise 1
let building = {
    numberLevels : 4,
    numberOfAptByLevel : {
        "1": 3,
        "2": 4,
        "3": 9,
        "4": 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        "Sarah": [3, 990],
        "Dan":  [4, 1000],
        "David": [1, 500],
    },
}

//Console.log the number of levels in the building.
console.log(building.numberLevels);
//Console.log how many apartments are on levels 1 and 3.
console.log(building.numberOfAptByLevel[1], building.numberOfAptByLevel[3]);
//Console.log the name of the second tenant and the number of rooms he has in his apartment.
console.log(building.nameOfTenants[1], building.numberOfRoomsAndRent.Dan[0]);
//Check if the sum of Sarah and David’s rent is bigger than Dan’s rent. If so, increase Dan's rent.
if ((building.numberOfRoomsAndRent.Sarah[1])+(building.numberOfRoomsAndRent.David[1]) > (building.numberOfRoomsAndRent.Dan[1])) {
    building.numberOfRoomsAndRent.Dan[1] = 1500;
}
console.log(building.numberOfRoomsAndRent.Dan[1]);

//Exercise 2
let numbers = [123, 8409, 100053, 333333333, 7]

//Loop through the array above and determine whether or not each number is divisible by three. Each time you loop console.log “true” or “false”.
for (i=0; i<numbers.length; i++) {
    if (numbers[i] %3 === 0) {
        console.log(numbers[i] + ": true");
    }
    else {
        console.log(numbers[i]+ ": false");
    }
}


//Exercise 3
let age = [20,5,12,43,98,55];

//Console.log the sum of all the numbers in the age array.
var sum = 0;
for (i=0; i<age.length; i++) {
    sum += age[i];
}
console.log(sum);

//Console.log the largest age in the array.
var big;
for (i=0; i<age.length; i++){
    if (age[i] > age[i+1]) {
        big = age[i];
    }
}
console.log(big);
