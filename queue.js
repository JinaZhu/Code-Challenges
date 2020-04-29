class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.first = null;
    this.last = null;
    this.length = 0;
  }
  peek() {
    return this.first;
  }
  enqueue(value) {
    const newNode = new Node(value);
    if (this.length === 0) {
      this.first = newNode;
      this.last = newNode;
    } else {
      this.last.next = newNode;
      this.last = newNode;
    }
    this.length++;
    return this;
  }
  dequeue() {
    if (this.length === 0) {
      return null;
    }
    if (this.first === this.last) {
      this.last = null;
    }
    this.first = this.first.next;
    this.length--;
    return this;
  }
  isEmpty() {
    if (this.length === 0) {
      return true;
    } else {
      return false;
    }
  }
}

const myQueue = new Queue();
myQueue.peek();
myQueue.enqueue("joy");
myQueue.enqueue("matt");
myQueue.enqueue("pavel");
console.log(myQueue.enqueue("Samir"));
console.log(myQueue.dequeue());

// create a constructor with a first and last array. Everytime you add to it, you reverse the array and add to the end and everytime you take from it, you reverse and take from the end

class CrazyQueue {
  constructor() {
    this.first = [];
    this.last = [];
  }
  enqueue(value) {
    const length = this.first.length;
    // loop through the amount of time as the length of first
    for (let i = 0; i < length; i++) {
      // add all item from first to last
      this.last.push(this.first.pop());
    }
    // add the new value to the end of the last list
    this.last.push(value);
    return this;
  }
  dequeue() {
    const length = this.last.length;
    // loop though the amount of time as the length of last
    for (let i = 0; i < length; i++) {
      // add all item from last to first
      this.first.push(this.last.pop());
    }
    this.first.pop();
    return this;
  }
  peek() {
    if (this.last.length > 0) {
      return this.last[0];
    }
    return this.first[this.first.length - 1];
  }
}

const myQueue2 = new CrazyQueue();
myQueue2.peek();
myQueue2.enqueue("Joy");
myQueue2.enqueue("Matt");
myQueue2.enqueue("Pavel");
myQueue2.peek();
myQueue2.dequeue();
myQueue2.dequeue();
myQueue2.dequeue();
myQueue2.peek();
