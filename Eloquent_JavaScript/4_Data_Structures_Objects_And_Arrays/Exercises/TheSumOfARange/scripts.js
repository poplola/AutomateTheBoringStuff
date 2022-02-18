/*
The sum of a range
The introduction of this book alluded to the following as a nice way to compute the sum of a range of numbers:
 console.log(sum(range(1, 10)));
Write a range function that takes two arguments, start and end, and returns an array containing all the numbers 
from start up to (and including) end.
Next, write a sum function that takes an array of numbers and returns the sum of these numbers. 
Run the example program and see whether it does indeed return 55.
As a bonus assignment, modify your range function to take an optional third argument that 
indicates the “step” value used when building the array. If no step is given, 
the elements go up by increments of one, corresponding to the old behavior. 
The function call range(1, 10, 2) should return [1, 3, 5, 7, 9]. 
Make sure it also works with negative step values so that range(5, 2, -1) produces [5, 4, 3, 2].
*/


// function range(startNumber, endNumber, step=1) {
//     console.log('')
//     console.log(`[${startNumber}, ${endNumber}, ${step}] ==> `)
//     let newArray = [];
//     if ((startNumber > endNumber) && (step < 0 )) {
//         for (let x = startNumber; x > endNumber; x += step) {
//             newArray.push(x);
//         }
//     } else if ((startNumber <= endNumber) && (step > 0 )) {
//         for (let x = startNumber; x <= endNumber; x += step) {
//             newArray.push(x);
//         }
//     } else {
//         return `Data invalid, can't create an array.`
//     }
//     return newArray
// }


// while num <= end if start <= end else num > end:
// newArray.append(num)
// num += step
// return newArray


function range(startNumber, endNumber, step=1) {
    console.log('')
    console.log(`[${startNumber}, ${endNumber}, ${step}] ==> `)
    let newArray = [];
    let num = startNumber
    console.log(`${startNumber} <= ${endNumber}?? ${(startNumber<=endNumber) ? num<=endNumber : num>endNumber}`)
    if ((step < 0 && startNumber < endNumber) || (step > 0 && startNumber > endNumber)){
        return "Valid data! Can't create an array!"
    }
        

    while ((startNumber<=endNumber) ? num<=endNumber : num>endNumber){
        newArray.push(num)
        num += step
    }
    // // if ((startNumber > endNumber) && (step < 0 )) {
    // //     for (let x = startNumber; x > endNumber; x += step) {
    // //         newArray.push(x);
    // //     }
    // // } else if ((startNumber <= endNumber) && (step > 0 )) {
    // //     for (let x = startNumber; x <= endNumber; x += step) {
    // //         newArray.push(x);
    // //     }
    // // } else {
    // //     return `Data invalid, can't create an array.`
    // // 
    return newArray
}
    

function sum(arr) {
    sumOfArray = 0;
    for(let i=0; i<arr.length; i++) {
        sumOfArray += arr[i];
    }
    return sumOfArray;
}


// console.log(sum(range(1, 10)));
console.log(range(1, 10, 2));
console.log(range(1, 10));
console.log(range(1, 20, 3));
console.log(range(15, 2, -3));
console.log(range(2, 5, -1));

const a=(a1, a2) => a1.concat(a2);

console.log(a([1,2], [4,5]))