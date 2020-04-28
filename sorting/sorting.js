const notSorted = [5, 2, 1, 9, 3, 8, 7, 4, 6];

// bubble sort
function bubbleSort(arr) {
  for (let i = 0; i < arr.length - 1; i++) {
    for (let j = 0; j < arr.length - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        let holder = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = holder;
      }
    }
  }
  return arr;
}

console.log(bubbleSort(notSorted));

// merge sort
function mergeSort(arr) {
  if (arr.length < 2) {
    return arr;
  }
  const middle = Math.floor(arr.length / 2);
  const arr1 = mergeSort(arr.slice(0, middle));
  const arr2 = mergeSort(arr.slice(middle));

  return makeMerge(arr1, arr2);
}

function makeMerge(arr1, arr2) {
  const result = [];

  while (arr1.length > 0 || arr2.length > 0) {
    if (arr1.length === 0) {
      result.push(arr2.shift());
    } else if (arr2.length === 0) {
      result.push(arr1.shift());
    } else if (arr1[0] < arr2[0]) {
      result.push(arr1.shift());
    } else {
      result.push(arr2.shift());
    }
  }
  return result;
}

console.log(mergeSort(notSorted));

// quick sort

function quickSort(arr) {
  if (arr.length < 2) {
    return arr;
  }

  const middle = Math.floor(arr.length / 2);
  const pivot = arr[middle];

  const low = [];
  const high = [];
  const equal = [];

  for (let item of arr) {
    if (item < pivot) {
      low.push(item);
    } else if (item > pivot) {
      high.push(item);
    } else {
      equal.push(item);
    }
  }
  return quickSort(low) + equal + quickSort(high);
}

console.log(quickSort(notSorted));
