const randomNumber = (from, to) => Math.floor(Math.random() * (to - from + 1)) + from;

const button = document.querySelector('#lib-button');
button.addEventListener('click', makeStory);

const story = document.querySelector('#story');

function makeStory(event) {
  event.preventDefault();

  const nounInput = document.querySelector('#noun');
  const personInput = document.querySelector('#person');
  const verbInput = document.querySelector('#verb');
  const adjectiveInput = document.querySelector('#adjective');
  const placeInput = document.querySelector('#place');

  const noun = nounInput.value;
  const adjective = adjectiveInput.value;
  const person = personInput.value;
  const verb = verbInput.value;
  const place = placeInput.value;

  if (noun.trim() !== '' && adjective.trim() !== '' && person.trim() !== '' && verb.trim() !== '' && place.trim() !== '') {
    const storyNumber = randomNumber(1,3);

    const funnyDialogueTemplate = `${person}: Hey, have you seen my ${noun}?\n${adjective} Friend: Yeah, I saw it in the ${place} near the ${noun}.\n${person}: What?! How did it end \
    up there?\n${adjective} Friend: I think it ${verb} its way there!`;
    const adventureStoryTemplate = `Once upon a time in a ${place}, there lived a ${adjective} ${noun} named ${person}. ${person} loved to ${verb} around the ${place} and discover \
    hidden treasures.`;
    const scaryStoryTemplate = `In a chilling ${place}, a ${adjective} ${noun} named ${person} used to ${verb} around. One night, ${person} decided to visit the ${place} again. \
    As ${person} entered, a cold wind sent shivers down their spine. The trees whispered eerie secrets, and a sense of ${adjective} fear enveloped them. Suddenly, a shadowy \
    figure emerged from the darkness, and ${person} felt their heart race. ${person} ran as fast as they could, their footsteps echoing through the ${place}. They finally \
    reached safety, vowing never to return to that ${adjective} place again.`;
    const storyVariants = [funnyDialogueTemplate, adventureStoryTemplate, scaryStoryTemplate];
    const storyContent = storyVariants[storyNumber];

    const storyParagraph = document.createElement('p');
    storyParagraph.textContent = storyContent;

    story.append(storyParagraph);
  } else {
    alert('Please fill out all the fields.');
  };
};