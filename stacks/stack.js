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

// const myStack2 = new stackArray();
// myStack2.push(1);
// myStack2.push(2);
// myStack2.push(3);
// myStack2.pop();

function asteroidCollision(asteroids) {
  const stack = [];
  let i = 0;

  while (i < asteroids.length) {
    let currentAsteroid = asteroids[i];
    const lastItem = stack.length - 1;

    // if stack is empty
    // or last item in stack is negative
    // or current item and last item in stack is positive
    if (
      stack.length === 0 ||
      stack[lastItem] < 0 ||
      (stack[lastItem] >= 0 && currentAsteroid >= 0)
    ) {
      // if so, add to the stack
      stack.push(currentAsteroid);
    } else {
      // if current item and last item in stack is equal
      if (Math.abs(currentAsteroid) === Math.abs(stack[lastItem])) {
        // remove last item of stack
        stack.pop();
        // if current item is greater than last item of stack, also remove
      } else if (Math.abs(currentAsteroid) > Math.abs(stack[lastItem])) {
        stack.pop();
        i--;
      }
    }
    i++;
  }
  return stack;
}

console.log("asteroidCollision", asteroidCollision([-2, -1, 1, 2]));
console.log("asteroidCollision", asteroidCollision([5, 10, -5]));
