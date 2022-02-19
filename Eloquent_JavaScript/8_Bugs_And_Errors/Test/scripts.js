"use strict";
// function Person(name) { this.name = name; }
// let ferdinand = Person("Ferdinand"); // forgot new
// // → TypeError: Cannot set property 'name' of undefined


// //============================== Testing
// function test(label, body) {
//     (!body()) ? console.log(`Failed: ${label}`) : console.log("Passed!");
// }
// test("convert Latin text to uppercase", () => { return "hello".toUpperCase() == "HELLO";});
// test("convert Greek text to uppercase", () => { return "Χαίρετε".toUpperCase() == "ΧΑΊΡΕΤΕ";});
// test("don't convert case-less characters", () => { return "مرحبا".toUpperCase() == "مرحبا"; });
    

// //============================== Debugging
// function numberToString(n, base = 10) { let result = "", sign = "";
// if (n < 0) {
// sign = "-";
// n = -n; }
//    do {
//      result = String(n % base) + result;
//      n = Math.floor(n / base);
// } while (n > 0);
// return sign + result;
// 132
// }
// console.log(numberToString(1398, 10), typeof numberToString(13, 10));


// //============================== Error propagation
// function promptNumber(question) {
//     let result = Number(prompt(question));
//     if (Number.isNaN(result)) return null;
//     else return result;
//  }
//  console.log(promptNumber("How many trees do you see?"));
 

//  function lastElement(array) {
//     if (array.length == 0) {
//       return {failed: true};
//     } else {
//       return {element: array[array.length - 1]};
//     }
//  }
//  console.log(lastElement([7,4,9,2]));


//============================== Exceptions
function promptDirection(question) {
    let result = prompt(question);
    if (result.toLowerCase() == "left") return "L"; 
    if (result.toLowerCase() == "right") return "R";
    throw new Error("Invalid direction: " + result);
}

function look() {
    if (promptDirection("Which way?") == "L") {
        return "a house"; 
    } else {
        return "two angry bears";

    }
}

try {
    console.log("You see", look());
} catch (error) {
    console.log("Something went wrong: " + error);
}


//============================== Selective catching
for (;;) {
    try {
        let dir = promptDirection("Where?"); // ← typo! console.log("You chose ", dir);
        break;
    } catch (e) {
    console.log("Not a valid direction. Try again.");
    } 
}
 

let a = [1,3,5,7,3];
for (let i in a) console.log(i)