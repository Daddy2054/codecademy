// Write your code here:

function dogFactory (name1, breed1, weight1) {
    let dog = {
    name : name1,
    breed : breed1,
    weight : weight1,
    };
    return dog;
}
    
dogFactory('Joe', 'Pug', 27);
// Should return { name: 'Joe', breed: 'Pug', weight: 27 }
