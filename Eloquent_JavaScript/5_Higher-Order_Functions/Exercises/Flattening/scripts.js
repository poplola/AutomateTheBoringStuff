/*
Flattening
Use the reduce method in combination with the concat method to “flatten” an array of arrays 
into a single array that has all the elements of the original arrays.
*/


// function reduce(array, combine, start) {
//     let current = start;
//     for (let element of array) {
//         current = current.concat(element);
//     }
//     console.log(current)
//     return current;
// }

myArr = [[1, 2, 3], [7, 8], [5, 6]];
console.log(myArr.reduce((a,b) => a.concat(b)));
console.log(typeof myArr.reduce((a,b) => a.concat(b)));