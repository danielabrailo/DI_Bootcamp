// Daily Challenge
let x = "*";
for (let i=0; i<6;i++) {
    console.log(x);
    x = x+"*";
}

// With nested loop
let star = "*";
console.log(star);
for (let i=0; i<6; i++){
    for(let g=0; g<6;g++) {
        if (i >= g){
        star = star + "*";                
        }

    }
    star = star + "\n";
}
console.log(star);