const _ = {
    clamp(number, lowerBound, upperBound) {
        return Math.min(Math.max(number, lowerBound),upperBound);
    },
    inRange(number, start, end) {
        if ( end == undefined) {
            end = start;
            start = 0;
        }
        if (start > end) {
            let temp = end;
            end = start;
            start = temp;
        }
        return (number >= start && number < end);
    },
    words (str) {
        return str.split(' ');
    },
    pad (str, len) {
        if (len > str.length) {
            let i = Math.floor((len-str.length)/2);
            return ' '.repeat(i) + str + ' '.repeat(len-str.length-i); 
        } else { return str;}
    } ,   
    has (obj, key) {
        let hasValue ; 
        if (obj[key] != undefined) {
            hasValue = true;
        } else {
            hasValue = false;
        }    
        return hasValue;
    },
    invert(obj) {
        let obj2 = {};
        for (const key in obj) {
            let val = obj[key];
            obj2[val] = key;
        }
        return obj2;
    },
    findKey (object, predicate) {
        for (const key in object) {
            const value = object[key];
            let predicateReturnValue = predicate(value);    
            if (predicateReturnValue) {
                return key;
            }
        }
        return undefined;
     },    
     drop (array, num) {
         if (num == undefined) {
             num = 1;
         }
         return array.slice(num);
     },
     dropWhile( array, predicate ) {
        let dropNumber = array.findIndex( (element, index) => !predicate(element, index, array));
        droppedArray = this.drop(array, dropNumber);
        return droppedArray;

//        func1(element, index) { return !predicate(element, index, array)}
    },

};

//2 - Returns an object with all keys and values inverted - Failed: 
_.invert({originalKey: "originalValue"}) ;
//returned undefined instead of originalKey.
// Do not write or modify code below this line.
module.exports = _;