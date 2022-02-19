/*
Retry

Say you have a function primitiveMultiply that in 20 percent of cases multiplies two numbers 
and in the other 80 percent of cases raises an exception of type MultiplicatorUnitFailure. 
Write a function that wraps this clunky function and just keeps trying until a call succeeds, 
after which it returns the result.

Make sure you handle only the exceptions you are trying to handle.

*/

// percents is from 0 ~ 99%
"use strict";

class MultiplicatorUnitFailure extends Error {}
function primitiveMultiply(num1 = 5, num2 = 4) {
    
    let percents;
    percents = Math.floor(Math.random() * 100);
    // console.log(percents);
    
    if (percents <= 19) {
        console.log(`Pass! you are in between 0% ~ 19%. (${percents}%)`)
        return num1 * num2;
    } else {
        throw new MultiplicatorUnitFailure(console.log(`Multiplicator Unit Failure! you are in 80% failure. (${percents}%)`))
    }
 
} 



try {
    console.log(primitiveMultiply());
} catch(MultiplicatorUnitFailure) {
    console.log("Something went wrong. Try again! ");
    // console.log(MultiplicatorUnitFailure)
    primitiveMultiply();
} 
// finally{
//     console.log("done!")
// }
