// Write your code here:

function convertToBaby(array) {
    let newarray = [];
    for (let index = 0; index < array.length; index++) {
        const element = array[index];
        newarray.push('baby '+element);
      } 
      console.log(newarray);

    }

const animals = ['panda', 'turtle', 'giraffe', 'hippo', 'sloth', 'human'];

console.log(convertToBaby(animals)) 
