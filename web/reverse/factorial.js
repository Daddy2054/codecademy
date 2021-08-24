/*Write a function factorial() that takes a number as an argument 
and returns the factorial of the number.
*/
function factorial(num) {
    let y = num;
    for (let index = num - 1; index > 0; index--) {
            y = y * index ; 
        }
    return y;        
}


console.log(factorial(1));
