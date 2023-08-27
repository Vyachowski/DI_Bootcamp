// Daily Challenge: Creating Objects
// InstructionsЖ
// In this exercise, you will use object oriented programming concepts to define and use a custom object in JavaScript.
// Create a class named Video. The class should be constructed with the following parameters:
// title (a string)
// uploader (a string, the person who uploaded it)
// time (a number, the duration of the video - in seconds)
// Create a method called watch() which displays a string as follows:
// “uploader parameter watched all time parameter of title parameter!”
class Video {
  constructor(title, uploader, time) {
    this.title = title;
    this.uploader = uploader;
    this.time = time;
  };

  watch() {
    return `${this.uploader} watched all ${this.time} of ${this.title}!`;
  }
}
// Instantiate a new Video instance and call the watch() method.
const iAmEatingBagle = new Video('Bagle', 'Slavik', 25);
// console.log(iAmEatingBagle.watch()); // -> Slavik watched all 25 of Bagle!
// Instantiate a second Video instance with different values.
const iAmBeatingEagle = new Video('Eagle', 'Slavik', 123);
// console.log(iAmBeatingEagle.watch()); // -> Slavik watched all 123 of Eagle!
// Bonus: Use an array to store data for five Video instances (ie. title, uploader, time)
const videos = [
  { title: "Video 1", uploader: "User", time: 10 },
  { title: "Video 2", uploader: "Userok", time: 110 },
  { title: "Video 3", uploader: "Useriks", time: 1110 },
  { title: "Video 4", uploader: "Userator", time: 1011 },
  { title: "Video 5", uploader: "Userman", time: 11110 },

];
// Think of the best data structure to save this information within the array.
// Bonus: Loop through the array to instantiate those instances.
const videoInstances = videos.map(video => new Video(video.title, video.uploader, video.time));
// console.log(videoInstances); // -> Array with instances of videos