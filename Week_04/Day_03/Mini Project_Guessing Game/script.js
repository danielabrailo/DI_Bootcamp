function playTheGame() {
    let result = confirm("Do you want to play the game?");
    if (!result) {
        alert("No problem, Goodbye");
    }
    else {
        let num = parseInt(prompt("Enter a number between 0 and 10"));
        if (num > 10 || num < 0) {
            alert("Sorry it’s not a good number, Goodbye");       
        }
        else if (!num) {
            alert("Sorry, not a number, Goodbye!");
        }
        else {
            let computerNumber = Math.floor(Math.random() * 11);
            test(num, computerNumber, 0);
        }
        
    }
}

function test(userNumber, computerNumber, count) {
    if (count === 3) {
        alert("Out of chances!");
        return;
    }
    else if (userNumber === computerNumber) {
        alert("WINNER!!");
        }
    else if (userNumber > computerNumber) {
        let result = parseInt(prompt("Your number is bigger then the computer’s, guess again"));
        count++;
        test(result,computerNumber, count);
    }
    else if (userNumber < computerNumber) {
        let result = parseInt(prompt("Your number is bigger then the computer’s, guess again"));
        count++;
        test(result,computerNumber, count);
    }
}

