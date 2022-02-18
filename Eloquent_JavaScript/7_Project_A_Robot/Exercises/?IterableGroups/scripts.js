/*
Iterable groups

Make the Group class from the previous exercise iterable. Refer to the section about 
the iterator interface earlier in the chapter if you aren’t clear on the exact form of the interface anymore.

If you used an array to represent the group’s members, don’t just return the iterator created by calling the Symbol.
iterator method on the array. That would work, but it defeats the purpose of this exercise.

It is okay if your iterator behaves strangely when the group is modified during iteration.
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

class GroupIterator {
    constructor(group) {
        this.group = group;
        this.x = 0;
        // console.log(this.x, Object.keys(this.group).length);
    }

    next() { 
        // console.log(this.group)
        // console.log(this.x, this.group.length);
        if (this.x == Object.keys(this.group).length) return {done: true};
        let value = {value: this.group[this.x]};
        this.x++
        return `{${this.x}, ${value}, done: false}`;
    }
}

Group.prototype[Symbol.iterator] = () => new GroupIterator(this);
// Group.prototype[Symbol.iterator] = () => new GroupIterator(this);
// Group[Symbol.iterator] = () => new GroupIterator(this);

const mySet = new Group();
let myIterator = mySet[Symbol.iterator]();
console.log(mySet.add(4));
console.log(mySet.add('4'));
console.log(myIterator.next())
console.log(mySet.add(14));
console.log(mySet.add(-5));
console.log(mySet.add(14));
console.log(myIterator.next());
console.log(mySet.delete(14));
console.log(mySet.delete(24));


console.log(mySet.has(4));
console.log(mySet.has(24));
console.log(mySet.has('4'));

console.log(myIterator.next())