const start_btn = document.getElementById("start_btn");
const timer_head = document.getElementById("timer_head");
const timer = document.getElementById("timer");

var exerciseTime = 10;
var round = 1;
var cycle = 2;

var min = "";
var sec = "";

let startMode = false;
let intervalTime = "";

//타이머를 시작한다.
function startTimer() {
  startMode = true;
  intervalTime = setInterval(function () {
    min = parseInt(exerciseTime / 60);
    sec = exerciseTime % 60;

    timer_head.innerHTML = "";
    timer.innerHTML = min + ":" + sec;
    exerciseTime--;

    if (exerciseTime < 0) {
      stopTimer();
      timer.innerHTML = "종료";
      start_btn.innerText = "시작";
    }
  }, 1000);
}

//타이머를 종료한다.
function stopTimer() {
  startMode = false;
  clearTimeout(intervalTime);
}

//타이머를 동작한다.
function handleTimerButton() {
  if (!startMode) {
    startTimer();
    start_btn.innerText = "정지";
  } else {
    stopTimer();
    start_btn.innerText = "시작";
  }
}
