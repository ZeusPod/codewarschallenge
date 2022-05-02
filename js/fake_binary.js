function fakeBin(x){
 let bin = x.split('')
 let result = []
    for (i = 0; i < bin.length; i++) {
        if (bin[i] <  5) {
            result.push(0)
        } else {
            result.push(1)
        }
    }
    return result.join('')
}

