function myMove() {
  var animate = document.getElementById("animate");
  var container = document.getElementById("container");
  var position = 0;

  var interval = setInterval(function() {
      if (position >= container.clientWidth - animate.clientWidth) {
          clearInterval(interval);
      } else {
          position++;
          animate.style.left = position + "px";
      }
  }, 1);
}