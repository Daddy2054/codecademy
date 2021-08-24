/*
Write a function groceries() that takes an array of object literals of grocery items.
 The function should return a string with each item separated by a comma except 
 the last two items should be separated by the word 'and'. 
 Make sure spaces (' ') are inserted where they are appropriate.
*/
function groceries(array) {
    let str = [];
    let sep1 = ', ';
    let sep2 = ' and ';
    for (let index = 0; index < array.length; index++) {
        str.push(sep1);
        str.push( array[index].item);        
    }
    str[str.length-2] = sep2;
    str.shift();
    return str.join('');
}

Examples:

groceries( [{item: 'Carrots'}, {item: 'Hummus'}, {item: 'Pesto'}, {item: 'Rigatoni'}] );
// returns 'Carrots, Hummus, Pesto and Rigatoni'
 
groceries( [{item: 'Bread'}, {item: 'Butter'}] );
// returns 'Bread and Butter'
 
groceries( [{item: 'Cheese Balls'}] );
// returns 'Cheese Balls'
