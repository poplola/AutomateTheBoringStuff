const makeNoise = function() {
    console.log("Ping!");
};
makeNoise();

const power = function(base, exponent){
    let result = 1;
    for (let count = 0; count < exponent; count++){
        result *=base;
    }
    return result;
};
console.log(power(2,10));

function power1(base, exponent) {
    if (exponent == 0) {
      return 1;
    } else {
      return base * power1(base, exponent - 1);
    }
 } 

console.log(power1(2,10));