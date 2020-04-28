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
