var time = 10;

var min = "";
var sec = "";

function handleTimerButton() {
  var x = setInterval(function () {
    min = parseInt(time / 60);
    sec = time % 60;

    document.getElementById("timer_head").innerHTML = "";
    document.getElementById("timer").innerHTML = min + ":" + sec;
    time--;

    if (time < 0) {
      clearInterval(x);
      document.getElementById("timer").innerHTML = "종료";
    }
  }, 1000);
}
