// // → The rabbit says 'I'm alive.'
// let rabbit = {};
// rabbit.speak = (line) => {
//     console.log(`The rabbit said '${line}'`)
// }
// rabbit.speak("I'm alive.")


// //==============================
// function speak(line) {
//     console.log(`The ${this.type} rabbit says '${line}'`);
//     }
// let whiteRabbit = {type: "white", speak}; 
// let hungryRabbit = {type: "hungry", speak};
// whiteRabbit.speak("Oh my ears and whiskers, " + "how late it's getting!");
// // → The white rabbit says 'Oh my ears and whiskers, how
// // late it's getting!'
// hungryRabbit.speak("I could use a carrot right now.");
// // → The hungry rabbit says 'I could use a carrot right now.'
// speak.call(hungryRabbit, "Burp!");


// //==============================
// function normalize() {
//     console.log(this.coords.map(n => n / this.length));
//  }
//  normalize.call({coords: [0, 2, 3], length: 5}); // → [0, 0.4, 0.6]


// //==============================
// let empty = {}; 
// console.log(empty.toString); // → function toString()...{} 
// console.log(empty.toString()); // → [object Object]



// //==============================
// console.log(Object.getPrototypeOf({}) ==Object.prototype); // → true 
// console.log(Object.getPrototypeOf(Object.prototype)); // → null
// console.log(Object.prototype);
// console.log(Object.getPrototypeOf({}));


// //==============================
// function Rabbit(type) {
//     this.type = type;
//   }
// Rabbit.prototype.speak = function(line) {
//     console.log(`The ${this.type} rabbit says '${line}'`); }; 
//  let weirdRabbit = new Rabbit("weird"); 
//  weirdRabbit.prototype.speak("Hello!!!")


//==============================
class Rabbit {
    constructor(type) {
      this.type = type;
    }
    speak(line) {
        console.log(`The ${this.type} rabbit says '${line}'`);
    } 
}
let killerRabbit = new Rabbit("killer"); 
let blackRabbit = new Rabbit("black");
// killerRabbit.speak("I am a killer Rabbit!")
// blackRabbit.speak("I am black.")

 

// //==============================
// let ages = {
//     Boris: 39,
//     Liang: 22,
//     Júlia: 62
//  }; 
//  console.log(`Júlia is ${ages["Júlia"]}`);// → Júlia is 62
//  console.log("Is Jack's age known?", "Jack" in ages); // → Is Jack's age known? false 
//  console.log("Is toString's age known?", "toString" in ages); // → Is toString's age known? true 
//  console.log(ages.prototype)
//  console.log(ages.getPrototypeOf);



// //==============================
// Rabbit.prototype.toString = function() { 
//     return `a ${this.type} rabbit`;
// };
// console.log(String(blackRabbit)); 
// // → a black rabbit



// //==============================

// let sym = Symbol("name"); 
// console.log(sym == Symbol("name")); 
// // → false
// console.log(sym); 
// console.log(Symbol("name")); 
// Rabbit.prototype[sym] = 55; 
// console.log(blackRabbit[sym]);
// // → 55



// //==============================
// const toStringSymbol = Symbol("toString"); 
// Array.prototype[toStringSymbol] = function() { 
// 	return `${this.length} cm of blue yarn`; }; 
// // Array.prototype[toStringSymbol] = () => `${this.length} cm of blue yarn`;
// console.log([1, 2].toString());
//  // → 1,2
// console.log([1, 2][toStringSymbol]());
// // → 2 cm of blue yarn 


// //==============================
// let okIterator = "I am OK!"[Symbol.iterator](); 
// // console.log(okIterator.next());
// // // → {value: "O", done: false} 
// // console.log(okIterator.next());
// // // → {value: "K", done: false} 
// // console.log(okIterator.next());

// console.log("I am OK!".length)
// let i = 0;
// while (i<=8) {
//     console.log(okIterator.next());
//     i++;
// }
// // → {value: undefined, done: true}


//==============================
class Temperature {
    constructor(celsius) {
      this.celsius = celsius;
    }
    get fahrenheit() {
      return this.celsius * 1.8 + 32;
    }
    set fahrenheit(value) {
      this.celsius = (value - 32) / 1.8;
    }
    static fromFahrenheit(value) {
      return new Temperature((value - 32) / 1.8);
 } 
}
 let temp = new Temperature(22); 
 console.log(temp.fahrenheit); 
 // → 71.6
 temp.fahrenheit = 86; 
 console.log(temp.celsius);
 // → 30


//==============================

//==============================

//==============================

//==============================

//==============================

//==============================

//==============================

//==============================

//==============================

//==============================

//==============================

//==============================

//==============================

//==============================