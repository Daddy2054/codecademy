// Write your code here:
function shoutGreetings(array) {
    let newarray = [];
    array.forEach(element => {
        newarray.push( element.toUpperCase() + '!');
    });    
    return newarray;
}

// Feel free to uncomment out the code below to test your function!

const greetings = ['hello', 'hi', 'heya', 'oi', 'hey', 'yo'];

console.log(shoutGreetings(greetings));
// Should print [ 'HELLO!', 'HI!', 'HEYA!', 'OI!', 'HEY!', 'YO!' ]

