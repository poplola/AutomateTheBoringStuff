// let day1 = {
//     squirrel: false,
//     events: ["work", "touched tree", "pizza", "running"]
//     }; 
// console.log(day1.squirrel); 
// // → false 
// console.log(day1.wolf);
// // → undefined
// day1.wolf = false; 
// console.log(day1.wolf);
// // → false


// // =========================
// let JOURNAL = [];
// function addEntry(events, squirrel) {
//     JOURNAL.push({events, squirrel});
// }

// addEntry(["work", "touched tree", "pizza", "running", "television"], false);
// addEntry(["work", "ice cream", "cauliflower", "lasagna", "touched tree", "brushed teeth"], false); 
// addEntry(["weekend", "cycling", "break", "peanuts",
// "beer"], true);
// console.log(JOURNAL)


// // =========================
// function phi(table) {
//     return (table[3] * table[0] - table[2] * table[1]) /
//       Math.sqrt((table[2] + table[3]) *
//                 (table[0] + table[1]) *
//                 (table[1] + table[3]) *
//                 (table[0] + table[2]));
//  }
//  console.log(phi([76, 9, 4, 1])); // → 0.068599434

//  function tableFor(event, journal) {
//     let table = [0, 0, 0, 0];
//     for (let i = 0; i < journal.length; i++) {
//       let entry = journal[i], index = 0;
//       if (entry.events.includes(event)) index += 1;
//       if (entry.squirrel) index += 2;
//       table[index] += 1;
//  }
//     return table;
//   }
//  console.log(tableFor("pizza", JOURNAL)); // → [76, 9, 4, 1]

// // =========================
// function journalEvents(journal) {
//     let events = [];
//         for (let entry of journal) {
//             for (let event of entry.events) {
//                 if (!events.includes(event)) {
//                     events.push(event);
//             }
//         } 
//     }
//     return events;
// }
// console.log(journalEvents(JOURNAL));


// // =========================
// for (let event of journalEvents(JOURNAL)) { 
//     console.log(event + ":", phi(tableFor(event, JOURNAL)));
// }


// for (let entry of JOURNAL) {
//     if (entry.events.includes("peanuts") &&
//     !entry.events.includes("brushed teeth")) { 
//         entry.events.push("peanut teeth");
//     } 
// }
// console.log(phi(tableFor("peanut teeth", JOURNAL))); // → 1

console.log("one tweeo three".indexOf("ee")); // → 11
