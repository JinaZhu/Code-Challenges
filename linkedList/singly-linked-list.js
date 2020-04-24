// What a linked list looks linked
// 10-->5-->16
// head: {
//     value: 10,
//     next: {
//         value: 5,
//         next: {
//             value: 16,
//             next: null
//         }
//     }
// }

// class to create a new node that has a value and next
class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class singlyLinkedList {
  // the constructor is the very first thing we will run
  // in this situtation, we will be creating the very first node for the linkedList
  constructor(value) {
    this.head = {
      value: value,
      next: null,
    };
    // with the first node, there is nothing following it, the tail will also be the head
    this.tail = this.head;
    // keep track of how many nodes
    this.length = 1;
  }
  append(value) {
    const newNode = new Node(value);

    this.tail.next = newNode;
    this.tail = newNode;
    this.length++;
    return this;
  }
  prepend(value) {
    const newNode = new Node(value);
    // newNode.next stores the current head
    newNode.next = this.head;
    // the head is reassign to newNode
    this.head = newNode;
    this.length++;
    return this;
  }
  insert(index, value) {
    // if index is out of range, use the append method to add to the end of the list
    if (index >= this.length) {
      return this.append(value);
    }
    // create a new node
    let newNode = new Node(value);
    // assign leader as the previous node of the wanted index
    const leader = this.traverseToIndex(index - 1);
    // store the leader's next item
    const holderPointer = leader.next;
    // with the next item safely stored, the leader's next item will be reassign to be the newNode
    leader.next = newNode;
    // assign the holderPointer to be the next item to the new added Node
    newNode.next = holderPointer;
    this.length++;
    return this;
  }
  traverseToIndex(index) {
    // create a counter
    let counter = 0;
    // assign a variable as the holder and start with the head as the first item
    let currentNode = this.head;
    // as long as the counter is not equal to the index
    while (counter !== index) {
      // reassign the currentNode to be the next node
      currentNode = currentNode.next;
      // increase the counter
      counter++;
    }
    return currentNode;
  }
}
