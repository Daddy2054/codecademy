// Write your code here:


function justCoolStuff(array1, array2) {
    let array3 = [];
    array1.filter(func); 

    array1.forEach(element => {
        if (array2.includes(element) && !array3.includes(element)) {
            array3.push(element);
        }
    });    
    array2.forEach(element => {
        if (array1.includes(element) && !array3.includes(element)) {
            array3.push(element);
        }
    });  
    return array3;
}
function func(stuff) {
    return true;
}

// Feel free to uncomment the code below to test your function

const coolStuff = ['gameboys', 'skateboards', 'backwards hats', 'fruit-by-the-foot', 'pogs', 'my room', 'temporary tattoos'];

const myStuff = [ 'rules', 'fruit-by-the-foot', 'wedgies', 'sweaters', 'skateboards', 'family-night', 'my room', 'braces', 'the information superhighway']; 

console.log(justCoolStuff(myStuff, coolStuff))
// Should print [ 'fruit-by-the-foot', 'skateboards', 'my room' ]

