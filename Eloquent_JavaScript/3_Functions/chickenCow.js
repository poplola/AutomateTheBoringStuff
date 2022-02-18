
// // ==== my own code
// function printFarmInventory(cows, chickens) {
//     let count = 3;
//     function printZeroPaddedWithLabel(animal, name) {
//       let animalDigits = String(animal).length;
//       for (animalDigits; animalDigits<count; animalDigits++) {
//           animal = "0" + animal; 
//       }
//       console.log(`${animal} ${name}`.toUpperCase())
//     }
//     printZeroPaddedWithLabel(cows, 'cows');
//     printZeroPaddedWithLabel(chickens, 'chickens');
//   }
// printFarmInventory(7, 11);



// // ==== book sample 1:
// function printFarmInventory(cows, chickens) {
//     let cowString = String(cows);
//     while (cowString.length < 3) {
//         cowString = "0" + cowString; 
//     }
//     console.log(`${cowString} Cows`);
//     let chickenString = String(chickens); 
//     while (chickenString.length < 3) {
//         chickenString = "0" + chickenString; 
//     }
//     console.log(`${chickenString} Chickens`); 
// }
// printFarmInventory(7, 11);



// // ==== book sample 2: better way
// function printZeroPaddedWithLabel(number, label) {
//     let numberString = String(number);
//     while (numberString.length < 3) {
//         numberString = "0" + numberString; 
//     }
//     console.log(`${numberString} ${label}`); 
// }
// function printFarmInventory(cows, chickens, pigs) { 
//     printZeroPaddedWithLabel(cows, "Cows"); 
//     printZeroPaddedWithLabel(chickens, "Chickens"); 
//     printZeroPaddedWithLabel(pigs, "Pigs");
// }
// printFarmInventory(7, 11, 3);



// ==== book sample 3: best way!
function zeroPad(number, width) {
    let string = String(number);
    while (string.length < width) {
        string = "0" + string; }
    return string;
}
function printFarmInventory(cows, chickens, pigs) { 
    console.log(`${zeroPad(cows, 3)} Cows`); 
    console.log(`${zeroPad(chickens, 3)} Chickens`); 
    console.log(`${zeroPad(pigs, 3)} Pigs`);
}
printFarmInventory(7, 16, 3);
 