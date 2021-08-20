let story = 'Last weekend, I took literally the most beautiful bike ride of my life. The route is called "The 9W to Nyack" and it actually stretches all the way from Riverside Park in Manhattan to South Nyack, New Jersey. It\'s really an adventure from beginning to end! It is a 48 mile loop and it basically took me an entire day. I stopped at Riverbank State Park to take some extremely artsy photos. It was a short stop, though, because I had a really long way left to go. After a quick photo op at the very popular Little Red Lighthouse, I began my trek across the George Washington Bridge into New Jersey.  The GW is actually very long - 4,760 feet! I was already very tired by the time I got to the other side.  An hour later, I reached Greenbrook Nature Sanctuary, an extremely beautiful park along the coast of the Hudson.  Something that was very surprising to me was that near the end of the route you actually cross back into New York! At this point, you are very close to the end.';

let overusedWords = ['really', 'very', 'basically'];

let unnecessaryWords = ['extremely', 'literally', 'actually' ];

let storyWords = story.split(' ');
//console.log(storyWords.length);
// step 3
let betterWords = storyWords.filter( word => {
    if (Boolean(unnecessaryWords.includes(word) == false)) {
        return word;
    }
});

//step 4
let overWords = {};
for (let i =0; i < overusedWords.length; i+=1){
    if (story.includes(overusedWords[i])) {
        let i2 = 0; //index
        let x = 0; // counter
        while (i2 != -1) {
            if (story.indexOf(overusedWords[i],i2) != -1) {
                overWords[overusedWords[i]]= x;
                x +=1;
                if (story.length >= i2 +1) {
                    i2 = story.indexOf(overusedWords[i],i2+1)
                }
            }
        }
    }
}
let sentenceCount = 0;
for (let i in storyWords) {
    if (storyWords[i][storyWords[i].length-1] == '.' || 
    storyWords[i][storyWords[i].length-1] == '!') {
        sentenceCount = sentenceCount += 1; 
    }
}
console.log(`Words count: ${storyWords.length}`)
console.log(`Sentences count: ${sentenceCount}` );
console.log('Overused words count:');
console.log(overWords);
console.log('\n');
console.log(betterWords.join(' '));

