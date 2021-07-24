//*Exercise 1
let personOne = {
    fullName: "John Doe",
    weigth: 80,
    height: 1.70,
    bmi: function() {
        return (this.weigth / (this.height ** 2)).toFixed(2);
    }
}

let personTwo = {
    fullName: "Alex Doe",
    weigth: 78,
    height: 1.65,
    bmi: function() {
        return (this.weigth / (this.height ** 2)).toFixed(2);
    }
};

personOne.bmi() > personTwo.bmi()? console.log(personOne.fullName + " has the largest BMI: " + personOne.bmi()) :  console.log(personTwo.fullName + " has the largest BMI: " + personTwo.bmi())
