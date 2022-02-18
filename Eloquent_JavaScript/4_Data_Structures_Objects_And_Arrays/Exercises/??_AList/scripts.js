/*
Write a function arrayToList that builds up a list structure like the one shown when given [1, 2, 3] as argument.
 Also write a listToArray function that produces an array from a list. 
 Then add a helper function prepend, which takes an element and a list and 
 creates a new list that adds the element to the front of the input list, and nth, 
 which takes a list and a number and returns the element at the given position in the list 
 (with zero referring to the first element) or undefined when there is no such element.
If you haven’t already, also write a recursive version of nth.
*/

// ?? result ==> (1, [2, [3, null]])

function arrayToList(arr) {
    let list = [];
    for (let i = 0; i< arr.length; i++) {
        list.append(i)
    }
    return list
}

myArr = [1,2,3];
console.log(arrayToList(myArr))