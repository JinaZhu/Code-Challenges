class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Stack {
  constructor() {
    this.top = null;
    this.bottom = null;
    this.length = 0;
  }
  peek() {
    return this.top;
  }
  push(value) {
    const newNode = new Node(value);

    if (this.length === 0) {
      this.top = newNode;
      this.bottom = newNode;
    } else {
      const holderPointer = this.top;
      this.top = newNode;
      this.top.next = holderPointer;
    }
    this.length++;
    return this;
  }
  pop() {
    if (!this.pop) {
      return null;
    }
    if (this.top === this.bottom) {
      this.bottom = null;
    }
    this.top = this.top.next;
    this.length--;
    return this;
  }
  isEmpty() {
    if (this.length === 0) {
      return true;
    } else {
      return this;
    }
  }
}

const myStack = new Stack();
console.log(myStack.isEmpty());
console.log(myStack.push("google"));
myStack.push("Udemy");
myStack.push("discord");
myStack.pop();
myStack.peek();

class stackArray {
  constructor() {
    this.array = [];
  }
  peek() {
    return this.array[this.array.length - 1];
  }
  push(value) {
    this.array.push(value);
    return this;
  }
  pop() {
    this.array.pop();
    return this;
  }
}

const myStack2 = new stackArray();
myStack2.push(1);
myStack2.push(2);
myStack2.push(3);
myStack2.pop();
