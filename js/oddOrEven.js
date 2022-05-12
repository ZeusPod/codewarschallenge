// Given a list of integers, determine whether the sum of its elements is odd or even.


function oddOrEven(array) {
    return array.reduce((acc, curr) => acc + curr, 0) % 2 === 0 ? 'even' : 'odd';
}

console.log(oddOrEven([0]));