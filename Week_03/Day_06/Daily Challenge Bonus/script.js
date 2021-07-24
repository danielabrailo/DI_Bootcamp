// Daily Challenge to practice bubble sort
const numbers = [5,0,9,1,7,4,2,6,3,8];

console.log(numbers.toString());
console.log(numbers.join(" "));

for (var i=0; i < numbers.length; i++){
    for (var j=0; j<(numbers.length -i -1); j++){

        // If the first number is smaller than the second they will be swapped 
        if (numbers[j] < numbers[j+1]){
            var temp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = temp
            console.log(numbers); // Showing the results on each time numbers are swapped
    }
}
}
console.log(numbers);
