// You have an endless supply of dimes and pennies. How many different amounts of total change can you make using exactly num_coins number coins?
// For example, when num_coins = 3, you can create 4 different kinds of change:

function numCoins(coins) {
  const result = new Set();

  for (let dimes = 0; dimes < coins + 1; dimes++) {
    let pennies = coins - dimes;
    result.add(dimes * 10 + pennies);
  }
  return result.size;
}

console.log("numCoins", numCoins(100));

// find the area of a polygon for a given n.

function polygonArea(num) {
  let count = 1;
  let addOn = 4;

  for (let i = 1; i < num; i++) {
    count += addOn;
    addOn += 4;
  }
  return count;
}

console.log("polygonArea", polygonArea(100));
console.log("polygonArea", polygonArea(2));

//Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

function intToRoman(num) {
  // order matters in this case
  const romanArr = [
    [1000, "M"],
    [900, "CM"],
    [500, "D"],
    [400, "CD"],
    [100, "C"],
    [90, "XC"],
    [50, "L"],
    [40, "XL"],
    [10, "X"],
    [9, "IX"],
    [5, "V"],
    [4, "IV"],
    [1, "I"],
  ];

  let result = "";

  while (num !== 0) {
    // check if item is greater than num and if so, add the item's second item to the result str and subtract the num by the item's first item
    for (const item of romanArr) {
      if (num >= item[0]) {
        result += item[1];
        num -= item[0];
        break;
      }
    }
  }
  return result;
}

console.log("intToRoman", intToRoman(1993));
