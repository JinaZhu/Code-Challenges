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
}

const tree = new BinarySearchTree();
tree.insert(10);
tree.insert(5);
tree.insert(15);
console.log(JSON.stringify(traverse(tree.root)));

// function to access all the nodes in a tree
function traverse(node) {
  // assign a variable to hold all the node
  const tree = { value: node.value };
  tree.left = node.left === null ? null : traverse(node.left);
  tree.right = node.right === null ? null : traverse(node.right);
  return tree;
}
