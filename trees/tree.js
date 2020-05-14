// Binary Search Tree

class Node {
  constructor(value) {
    this.left = null;
    this.right = null;
    this.value = value;
  }
}

class BinarySearchTree {
  constructor() {
    this.root = null;
  }

  insert(value) {
    const newNode = new Node(value);

    if (!this.root) {
      this.root = newNode;
    } else {
      let currentNode = this.root;
      // use true to keep looping
      while (true) {
        // if the value is less than the currentNode
        if (value < currentNode.value) {
          // is there an element to the left
          if (!currentNode.left) {
            // if currentNode.left is empty, there's a spot for currentNode
            currentNode.left = newNode;
            // will end loop
            return this;
            // if there is something at that position, assign it as the new currentNode
          } else {
            currentNode = currentNode.left;
          }
        } else {
          if (!currentNode.right) {
            currentNode.right = newNode;
            return this;
          } else {
            currentNode = currentNode.right;
          }
        }
      }
    }
  }

  lookup(value) {
    if (!this.root) {
      return false;
    }
    let currentNode = this.root;
    // the while loop will keep going as long as there is a currentNode to check
    while (currentNode) {
      if (value < currentNode.value) {
        currentNode = currentNode.left;
      } else if (value > currentNode.value) {
        currentNode = currentNode.right;
      } else if (currentNode.value === value) {
        return currentNode;
      }
    }
    return false;
  }
  remove(value) {
    if (!this.root) {
      return false;
    }
    let currentNode = this.root;
    // reference to parent
    let parentNode = null;
    // as long as there is a currentNode
    while (currentNode) {
      // option 1: if value is less than currentNode, go left
      if (value < currentNode.value) {
        parentNode = currentNode;
        currentNode = currentNode.left;
        // if value is greater than currentNode, go right
      } else if (value > currentNode.value) {
        parentNode = currentNode;
        currentNode = currentNode.right;
        // we found the value!
      } else if (currentNode.value === value) {
        // if there is no right child
        if (currentNode.right === null) {
          // if parentNode is nothing, the root will be the currentNode.left
          if (parentNode === null) {
            this.root = currentNode.left;
            // if parent is not null
          } else {
            // if parent is greater than current, make current left child a child of parent
            if (currentNode.value < parentNode.value) {
              parentNode.left = currentNode.left;
              // if parent < current value make left child a right child of parent
            } else if (currentNode.value > parentNode.value) {
              parentNode.right = currentNode.left;
            }
          }
          // option 2: right child doesnt have a left child
        } else if (currentNode.right.left === null) {
          if (parentNode === null) {
            this.root = currentNode.left;
          } else {
            currentNode.right.left = currentNode.left;
            // if current is less than parent, parent left is assign to currentNode.right
            if (currentNode.value < parentNode.value) {
              parentNode.left = currentNode.right;
              // if current is greater than parent, parent right is assign to currentNode.right
            } else if (currentNode.value > parentNode.value) {
              parentNode.right = currentNode.right;
            }
          }
          // option 3: if current right has a left
        } else {
          let leftmost = currentNode.right.left;
          let leftmostParent = currentNode.right;
          // as long as leftmost.left is not null
          while (leftmost.left !== null) {
            leftmostParent = leftmost;
            leftmost = leftmost.left;
          }
          leftmostParent.left = leftost.right;
          leftmost.left = currentNode.left;
          leftmost.right = currentNode.right;

          if (parentNode === null) {
            this.root = leftmost;
          } else {
            if (currentNode.value < parentNode.value) {
              parentNode.left = leftmost;
            } else if (currentNode.value > parentNode.value) {
              parentNode.right = leftmost;
            }
          }
        }
        return true;
      }
    }
  }
  breadthFirstSearch() {
    let currentNode = this.root;
    let list = [];
    // queue to keep track of the level we are at the access the childreds
    let queue = [];
    queue.push(currentNode);
    // as long as there is nothing left at the queue
    while (queue.length > 0) {
      //assign currentNode to be the first item from the queue
      currentNode = queue.shift();
      // pushing it into the list
      list.push(currentNode.value);
      if (currentNode.left) {
        queue.push(currentNode.left);
      }
      if (currentNode.right) {
        queue.push(currentNode.right);
      }
    }
    return list;
  }
}

const tree = new BinarySearchTree();
tree.insert(10);
tree.insert(5);
tree.insert(15);
console.log(tree.lookup(100));
console.log(tree.lookup(10));
// console.log(JSON.stringify(traverse(tree.root)));

// function to access all the nodes in a tree
function traverse(node) {
  // assign a variable to hold all the node
  const tree = { value: node.value };
  tree.left = node.left === null ? null : traverse(node.left);
  tree.right = node.right === null ? null : traverse(node.right);
  return tree;
}

console.log(tree.breadthFirstSearch());
