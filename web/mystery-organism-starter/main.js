// Returns a random DNA base
const returnRandBase = () => {
  const dnaBases = ['A', 'T', 'C', 'G'];
  return dnaBases[Math.floor(Math.random() * 4)];
};

// Returns a random single stand of DNA containing 15 bases
const mockUpStrand = () => {
  const newStrand = [];
  for (let i = 0; i < 15; i++) {
    newStrand.push(returnRandBase());
  }
  return newStrand;
};

const pAequorFactory = (specimanNum, dna) => {
  return {
    specimanNum,
    dna,
    mutate() {
      const randIndex = Math.floor(Math.random() * this.dna.length);
      let newBase = returnRandBase();
      while (this.dna[randIndex] === newBase) {
        newBase = returnRandBase();
      }
      this.dna[randIndex] = newBase;
      return this.dna;
    },
    compareDNA(pAequor) {
      let common = 0;
      for (let index = 0; index < this.dna.length; index++) {
          if (this.dna[index] == pAequor.dna[index]) {
            common++ ; 
          }  
      } 
      let percentage = ((common /  this.dna.length) * 100).toFixed(0);
      console.log(`specimen ${this.specimanNum} and specimen ${pAequor.specimanNum} have ${percentage}% DNA in common`)
    },
    willLikelySurvive() {
      let c_and_g = 0;
      let percentage ;
      for (let index = 0; index < this.dna.length; index++) {
        if (this.dna[index] == 'C' || this.dna[index] == 'G') {
          c_and_g++ ;
        }
        percentage = ((c_and_g /  this.dna.length) * 100).toFixed(0);
      }
      return (percentage >= 60);
    },
  };
}

const good_instances = [];
let index = 1 ;
while (good_instances.length < 30) {
    let pAequor = pAequorFactory(index,mockUpStrand());
    if (pAequor.willLikelySurvive()) {
      good_instances.push(pAequor);
      index++ ;
    }
}  
  
console.log(good_instances);


