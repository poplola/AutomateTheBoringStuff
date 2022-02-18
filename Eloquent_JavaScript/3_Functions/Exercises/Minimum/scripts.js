/*
Minimum
The previous chapter introduced the standard function Math.min that returns its smallest argument. 
We can build something like that now. Write a function min that takes two arguments and returns their minimum.
*/

function mininumNumber(num1, num2) {
    if (num1 >= num2) {
        return num2;
    } else {
        return num1;
    } 
}
console.log(`The mininum number is ${mininumNumber(9, 9)}.`)
console.log(Math.min(9,9))