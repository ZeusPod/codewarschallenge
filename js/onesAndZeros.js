const binaryArrayToNumber = arr => {
    return arr.reduce((acc, curr, index) => {
        return acc + curr * Math.pow(2, arr.length - index - 1);
    }, 0);
};