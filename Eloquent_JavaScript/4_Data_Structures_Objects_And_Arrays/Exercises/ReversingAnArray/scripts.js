/*
Reversing an array

Arrays have a reverse method that changes the array by inverting the order in which its elements appear. 
For this exercise, write two functions, reverseArray and reverseArrayInPlace. 

The first, reverseArray, takes an array as argument and produces a new array that has the same elements 
in the inverse order. 

The second, reverseArrayInPlace, does what the reverse method does: it modifies the array given as argument 
by reversing its elements. Neither may use the standard reverse method.

Thinking back to the notes about side effects and pure functions in the previous chapter, 
which variant do you expect to be useful in more situations? Which one runs faster?
*/


// function reverseArray()

function newArr() {
    myArr = [];
    step = 3
    for (let i = 1; i <= 9; i+=step) {
        myArr.push(i);
    }
    return myArr;
}

function reverseArray(arr) {
    reverseArr = [];
    arrLength = arr.length;
    for (let i = 0; i < arrLength; i++) {
        reverseArr.push(arr.pop(i))
    }
    return reverseArr;
}

function reverseArrayInPlace(arr) {

    midLengthOfArr = Math.floor(arr.length / 2);
    lengthOfArr = arr.length - 1

    for (let i = 0; i <= midLengthOfArr; i++ ) {
        tempData = arr[i];
        arr[i] = arr[lengthOfArr - i];
        arr[lengthOfArr - i] = tempData;
    }
    return arr;
}

let myArray = newArr();
console.log(myArray)
console.log(reverseArray(myArray));
console.log(myArray)
console.log(reverseArrayInPlace(newArr()));
