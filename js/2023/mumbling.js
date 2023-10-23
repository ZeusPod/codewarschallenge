function accum(s) {
    letters = s.split("")
    let result = letters.map((letter, index) => {
        return letter.toUpperCase() + letter.toLowerCase().repeat(index)
    })
    return result.join("-")
}

console.log(accum("abcd"))