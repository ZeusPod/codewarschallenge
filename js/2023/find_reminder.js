function find_reminder(a,b) {
    let result = 0 
    a > b ? result = a % b : result = b % a
    //redondiamos el resultado hacia el entero mas cercano inferior
    return Math.floor(result)
}


console.log(find_reminder(17,5))