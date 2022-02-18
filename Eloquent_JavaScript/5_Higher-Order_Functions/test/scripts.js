function repeat(n, action) {
    for (let i = 0; i < n; i++) {
 action(i); }
 }
  repeat(3, console.log);
  // → 0
  // → 1
  // → 2
 


// let labels = [];
// repeat(5, i => {
//     labels.push(`Unit ${i + 1}`); 
// });
// console.log(labels);
//  // → ["Unit 1", "Unit 2", "Unit 3", "Unit 4", "Unit 5"]



// function greaterThan(n) {
//     return m => m > n;
//  }
//  let greaterThan10 = greaterThan(10); 
//  console.log(greaterThan10(11));
//  // → true



//  // And we can have functions that change other functions.
// function noisy(f) {
//     return (...args) => {
//         console.log("calling with", args);
//         let result = f(...args);
//         console.log("called with", args, ", returned", result); 
//         return result;
//     };
// }
// noisy(Math.min)(3, 2, 1);
// // → calling with [3, 2, 1]
// // → called with [3, 2, 1] , returned 1



// We can even write functions that provide new types of control flow.
function unless(test, then) {
   if (!test) then();
}

repeat(3, n => {
    unless(n % 2 == 1, () => {
    console.log(n, "is even"); });
});
// → 0 is even // → 2 is even



["A", "B"].forEach(l => console.log(l)); 
// → A
// → B



console.log([1, 2, 3, 4].reduce((a, b) => a + b));
// → 10


function characterCount(script) {
    return script.ranges.reduce((count, [from, to]) => {
      return count + (to - from);
    }, 0);
 }
  console.log(SCRIPTS.reduce((a, b) => {
    return characterCount(a) < characterCount(b) ? b : a;
 }));
 // → {name: "Han", ...}