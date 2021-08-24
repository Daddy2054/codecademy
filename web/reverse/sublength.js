/*Write a function subLength() that takes 2 parameters, 
a string and a single character. The function should search the string 
for the two occurrences of the character and return the length between 
them including the 2 characters. If there are less than 2 or more than 2 
occurrences of the character the function should return 0.

*/
function subLength(str,char) {
    let x , y, z ;
    x = str.indexOf(char);
    y = str.indexOf(char,x+1);
    z = str.indexOf(char,y+1);
    if ( z > 0 ) { return 0;}  
    if ( y > 0) {
        return  y - x + 1;
    } else { return 0;}
}


//Examples:

subLength('Saturday', 'a'); // returns 6
subLength('summer', 'm'); // returns 2
subLength('digitize', 'i'); // returns 0
subLength('cheesecake', 'k'); // returns 0