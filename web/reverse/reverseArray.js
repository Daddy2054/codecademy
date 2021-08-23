function reverseArray( sentence) {
    let sent2 = [];
    for (let i = sentence.length; i >0; i--) {
        sent2.push(sentence.pop());
    }
    sentence = sent2
    return sentence
}   



const sentence = ['sense.','make', 'all', 'will', 'This'];
console.log(sentence) 
console.log(reverseArray(sentence))
//console.log(sentence) 
// Should print ['This', 'will', 'all', 'make', 'sense.'];
