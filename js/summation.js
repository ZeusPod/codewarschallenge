/* Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
 */

var summation = function(num) {
    var sum = 0 ;
    for (var i=0; i <= num; i++){
        sum += i;
    }
    return sum
}


mysum = summation(8)
console.log(mysum)