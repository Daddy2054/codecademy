// Write your code here:

function dogFactory (name1, breed1, weight1) {
    let dog = {
    _name : name1,
    get name() { return this._name;},
    set name(newname) { this._name = newname;},
    _breed : breed1,
    get breed() { return this._breed;},
    set breed(newbreed) { this._breed = newbreed;},
    _weight : weight1,
    get weight() { return this._weight;},
    set weight(newweight) { this._weight = newweight;},
    bark() { return 'ruff! ruff!'; },
    eatTooManyTreats() { this._weight += 1;},
};
    return dog;
}
    
dogFactory('Joe', 'Pug', 27);
// Should return { name: 'Joe', breed: 'Pug', weight: 27 }
