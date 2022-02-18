/*
Groups

The standard JavaScript environment provides another data structure called Set. Like an instance of Map, 
a set holds a collection of values. Unlike Map, it does not associate other values with those—it just tracks 
which values are part of the set. A value can be part of a set only once—adding it again doesn’t have any effect.

Write a class called Group (since Set is already taken). Like Set, it has add, delete, and has methods. 
Its constructor creates an empty group, add adds a value to the group (but only if it isn’t already a member), 
delete removes its argument from the group (if it was a member), and has returns a Boolean value indicating 
whether its argument is a member of the group.

Use the === operator, or something equivalent such as indexOf, to determine whether two values are the same.

Give the class a static from method that takes an iterable object as argument and creates a group that contains all the values produced by iterating over it.
*/

class Group {
    constructor () {
        this.set = []
    }

    add = (x) => {
        this.set.findIndex(c => c === x) == -1 ? this.set.push(x) : console.log(`Add Data Faild! ${x} is already in set [${this.set}]`);
        return this.set;
    }

    delete = (x) => {
        this.set.findIndex(c => c === x) == -1 ? console.log(`Delete Data Faild! No data ${x} in set [${this.set}]`) : this.set.splice(this.set.indexOf(x),1);
        return this.set
    }

    has = (x) => this.set.findIndex(c => c === x) == -1 ? false : true;
}

const mySet = new Group();
console.log(mySet.add(4));
console.log(mySet.add('4'));
console.log(mySet.add(14));
console.log(mySet.add(-5));
console.log(mySet.add(14));
console.log(mySet.delete(14));
console.log(mySet.delete(24));
console.log(mySet.has(4));
console.log(mySet.has(24));
console.log(mySet.has('4'));