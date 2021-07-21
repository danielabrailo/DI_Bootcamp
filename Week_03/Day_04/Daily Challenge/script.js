var sentence = "This ice-cream is bad";
var wordNot = sentence.indexOf("not");
var wordBad = sentence.indexOf("bad");

if (sentence.includes("bad") && sentence.includes("not") && wordBad > wordNot) {
    var str = sentence.substring(wordNot,wordBad+3);
    console.log(sentence.replace(str, "good"));
}
else {
    console.log(sentence);
}