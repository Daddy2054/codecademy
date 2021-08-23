const numbers = [2, 7, 9, 171, 52, 33, 14]

const toSquare = num => num * num

let num2 = [];

function squareNums(array){
  num2 = array.map(toSquare);
  return num2;
}

console.log(squareNums(numbers));
