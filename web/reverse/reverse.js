// Write your code here:
function sortStrR(sentence) {
    let i = 1;
    while (i < sentence.length) {
        x=sentence[i ];
        j=i-1;
        while (j >= 0 && sentence[j].charCodeAt(0) < x.charCodeAt(0)) {
            sentence[ j + 1 ] = sentence[ j ];
            j = j - 1;
        }
        sentence[j +1] = x ;
        i = i + 1;
    }    
    return sentence
}

function sortR(sentence) {
    let i = 1;
    while (i < sentence.length) {
        x=sentence[i ];
        j=i-1;
        while (j <= sentence.length && sentence[j] < x) {
            sentence[ j + 1 ] = sentence[ j ];
            j = j - 1;
        }
        sentence[j +1] = x ;
        i = i + 1;
    }    
    return sentence
}
function sort(sentence) {
    let i = 1;
    while (i < sentence.length) {
        x=sentence[i];
        j=i-1;
        while (j>=0 && sentence[j]>x) {
            sentence[j+1]=sentence[j];
            j=j-1;
        }
        sentence[j+1]=x;
        i = i +1;
    }    
    return sentence
}

//let sentence = [34,4565,567,33,568,35,68,89,234,445,67,85,3,23,5];
let sentence = ['sense.','make', 'all', 'will', 'This'];

console.log(sentence);
console.log(sortStrR(sentence));
/*

// When you're ready to test your code, uncomment the below and run:

const sentence = ['sense.','make', 'all', 'will', 'This'];

reverseArray(sentence)
console.log(sentence) 
// Should print ['This', 'will', 'all', 'make', 'sense.'];

*/

