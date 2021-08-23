// Write your code here:

function greetAliens(array) {
    for (let index = 0; index < array.length; index++) {
        const element = array[index];
        console.log('Oh powerful ' + element + ', we humans offer our unconditional surrender!') 
      } 
      }

// When you're ready to test your code, uncomment the below and run:

const aliens = ["Blorgous", "Glamyx", "Wegord", "SpaceKing"];

greetAliens(aliens);

/*
// Should print:
// Oh powerful Blorgous, we humans offer our unconditional surrender! 
// Oh powerful Glamyx, we humans offer our unconditional surrender! 
// Oh powerful Wegord, we humans offer our unconditional surrender! 
// Oh powerful SpaceKing, we humans offer our unconditional surrender! 
*/