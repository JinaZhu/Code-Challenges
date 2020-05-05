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

console.log(numCoins(100));
