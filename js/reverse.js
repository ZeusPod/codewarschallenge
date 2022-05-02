function reverseWords(str){
    reverse = str.split(" ")
    for (var i = 0; i < reverse.length; i++) {
        reverse[i] = reverse[i].split("").reverse().join("");
    }
    return reverse.join(" ");
}


myreverse = reverseWords("The quick brown fox jumps over the lazy dog.");
console.log(myreverse);