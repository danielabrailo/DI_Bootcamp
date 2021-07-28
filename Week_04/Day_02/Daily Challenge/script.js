let words = prompt("Write several words separated by a coma").split(", ");

let longestWord="";
for (i=0; i<words.length; i++){
    if (words[i].length > longestWord.length) {
        longestWord = words[i];
    }
}
console.log("*".repeat(longestWord.length+2));

for (i=0; i<words.length;i++){
    console.log("* "+ words[i]+ (" ".repeat(longestWord.length-(words[i].length)))+ "*");
}

console.log("*".repeat(longestWord.length+2));
