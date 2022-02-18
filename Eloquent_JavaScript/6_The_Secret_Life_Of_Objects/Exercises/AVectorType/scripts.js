/*
A vector type

Write a class Vec that represents a vector in two-dimensional space. It takes x and y parameters (numbers), 
which it should save to properties of the same name.

Give the Vec prototype two methods, plus and minus, that take another vector as a parameter and return 
a new vector that has the sum or difference of the two vectors’ (this and the parameter) x and y values.

Add a getter property length to the prototype that computes the length of the vector—that is, 
the distance of the point (x, y) from the origin (0, 0).
*/

class Vec {
    constructor (x, y) {
        this.x = x;
        this.y = y;
    }
    plus = (vecX, vecY) => `Sum of two vectors (${this.x}, ${this.y}) and (${vecX}, ${vecY}) ==> (${this.x + vecX}, ${this.y + vecY})`;

    minus = (vecX, vecY) => `Difference of two vectors (${this.x}, ${this.y}) and (${vecX}, ${vecY}) ==> (${this.x - vecX}, ${this.y - vecY})`;

    get getPointDistance() {
        return `The distance of the point (${this.x}, ${this.y}) from the origin (0, 0) ==> (${Math.abs(this.x)}, ${Math.abs(this.y)}) `;
    }

}

const vec1 = new Vec(-4,-8);
console.log(vec1.plus(2,5));
console.log(vec1.minus(9,3))
console.log(vec1.getPointDistance)