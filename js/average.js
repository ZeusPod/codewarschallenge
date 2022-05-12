// write a function which takes an array of numbers and returns the average


function average(array) {
    let sum = 0
    if (array.length > 0) {
    for (let i=0; i<array.length; i++) {
        sum += array[i]
    }
    return sum / array.length
    } else {
        return 0
    }
}

console.log(average([])); // 0