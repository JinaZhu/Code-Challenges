// Write a function that reverse characters inside paraentheses in a given string and return a new string with characters inside parentheses reversed and parentheses removed
// (bar) >> rab, foo(bar)baz >> foorabbaz, foo(bar(baz))blim >> foobazrabblim

function reverseInParentheses(str) {
  // keep function running as long as there is an opening bracket
  while (str.indexOf("(") !== -1) {
    str = reverseP(str);
  }
  return str;
}

function reverseP(str) {
  let len = str.length;

  // find the last opening bracket
  let openBracketInt = str.lastIndexOf("(");
  // the characters before the opening bracket
  let beforeBracket = str.slice(0, openBracketInt + 1);
  // the characters after the opening bracket
  let afterBracket = str.slice(openBracketInt + 1, len);

  // using the length of before bracket plus the index of the first occurance of the closing bracket to find the index of the closing bracket of the opening bracket
  let closeBracketInd = beforeBracket.length + afterBracket.indexOf(")");

  // slice the part before the opening, the part after the closing and the part inside the () and remove the ()
  let firstPart = str.slice(0, openBracketInt);
  let secondPart = str.slice(closeBracketInd + 1, len);
  let middle = str.slice(openBracketInt + 1, closeBracketInd);

  // reverse the string between the brackets
  middle = middle.split("").reverse().join("");

  return firstPart + middle + secondPart;
}

const a = "(abc)d(efg)";
console.log(reverseInParentheses(a));
