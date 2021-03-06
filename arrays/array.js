// You are given an array of integers a. A new array b is generated by
// rearranging the elements of a in the following way:

// b[0] is equal to a[0];
// b[1] is equal to the last element of a;
// b[2] is equal to a[1];
// b[3] is equal to the second-last element of a;
// and so on.
// Your task is to determine whether the new array b is sorted in strictly ascending order or not

function mergeStrings(s1, s2) {
  let newS1 = s1.split("");
  let newS2 = s2.split("");
  const countS1 = {};
  const countS2 = {};
  let newWord = "";

  for (let char of s1) {
    if (countS1[char]) {
      countS1[char]++;
    } else {
      countS1[char] = 1;
    }
  }
  for (let char of s2) {
    if (countS2[char]) {
      countS2[char]++;
    } else {
      countS2[char] = 1;
    }
  }

  while (newS1.length !== 0 || newS2.length !== 0) {
    if (newS1.length === 0) {
      newWord += newS2.shift();
    } else if (newS2.length === 0) {
      newWord += newS1.shift();
    } else if (countS1[newS1[0]] === countS2[newS2[0]]) {
      if (newS1[0] > newS2[0]) {
        newWord += newS2.shift();
      } else {
        newWord += newS1.shift();
      }
    } else if (countS1[newS1[0]] > countS2[newS2[0]]) {
      newWord += newS2.shift();
    } else if (countS1[newS1[0]] < countS2[newS2[0]]) {
      newWord += newS1.shift();
    }
  }
  return newWord;
}

console.log(mergeStrings("super", "tower"));
console.log(mergeStrings("aabb", "abab"));
console.log(mergeStrings("apple", "pie"));

function alternatingSort(a) {
  const b = [];
  count = 0;

  while (a.length !== 0) {
    if (count % 2 === 0) {
      b.push(a.shift());
      count++;
    } else {
      b.push(a.pop());
      count--;
    }
  }

  let anotherB = b.slice();
  console.log(b);
  console.log(JSON.stringify(anotherB.sort((a, b) => a - b)));
  if (JSON.stringify(anotherB.sort((a, b) => a - b)) === JSON.stringify(b)) {
    return true;
  } else {
    return false;
  }
}

console.log(alternatingSort([1, 3, 5, 6, 4, 2]));
console.log(alternatingSort([1, 2, 5, 6, 4, 3]));

// return a list of all characters that show up in all strings within the list (including duplicates).

function commonChar(wordArr) {
  let previousWord = wordArr[0].split("");

  for (let i = 1; i < wordArr.length; i++) {
    let currentWord = [];
    for (let char of wordArr[i]) {
      if (previousWord.includes(char)) {
        currentWord.push(char);
        let charIndex = previousWord.indexOf(char);
        previousWord.splice(charIndex, 1);
      }
    }
    previousWord = currentWord;
  }
  return previousWord;
}

console.log("commonChar", commonChar(["bella", "label", "roller"]));
console.log("commonChar", commonChar(["cool", "lock", "cook"]));

// An array is monotonic if it is either monotone increasing or monotone decreasing.

function isMontonic(num_arr) {
  for (let i = 0; i < num_arr.length - 1; i++) {
    if (num_arr[0] <= num_arr[num_arr.length - 1]) {
      if (num_arr[i] <= num_arr[i + 1]) {
        continue;
      } else {
        return false;
      }
    }
    if (num_arr[0] >= num_arr[num_arr.length - 1]) {
      if (num_arr[i] >= num_arr[i + 1]) {
        continue;
      } else {
        return false;
      }
    }
  }
  return true;
}

console.log("isMontonic", isMontonic([3, 4, 2, 3]));

// Given an array, rotate the array to the right by k steps, where k is non-negative.

function rotateArray(nums, steps) {
  newNums = [...nums];

  for (let i = 0; i < nums.length; i++) {
    if (i >= nums.length - steps) {
      newIndex = (i + steps) % nums.length;
      nums[newIndex] = newNums[i];
    } else {
      nums[i + steps] = newNums[i];
    }
  }
  return nums;
}

console.log("rotateArray", rotateArray([1, 2, 3, 4, 5, 6, 7], 3));

// Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

function addOne(nums) {
  // searching backwards
  let index = nums.length - 1;

  while (index >= 0) {
    // if current item is 9, change it to 0
    if (nums[index] === 9) {
      nums[index] = 0;
      index -= 1;
    } else {
      break;
    }
  }
  // index = -1 means all number is 9
  if (index === -1) {
    nums[0] = 1;
    nums.push(0);
    return nums;
  }
  // increase current item
  nums[index] += 1;

  return nums;
}

console.log("addOne", addOne([1, 2, 3]));
console.log("addOne", addOne([9, 9, 9]));
console.log("addOne", addOne([9]));

// You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees (clockwise).
function rotate(matrix) {
  for (let i = 0; i < matrix.length; i++) {
    // j should start at i index
    for (let j = i; j < matrix[i].length; j++) {
      // store the assign item
      let temp = matrix[i][j];
      matrix[i][j] = matrix[j][i];
      matrix[j][i] = temp;
    }
  }
  for (let row of matrix) {
    row.reverse();
  }
  return matrix;
}

console.log(
  "rotate",
  rotate([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
  ])
);
