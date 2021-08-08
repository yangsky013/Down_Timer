const start_btn = document.getElementById("start_btn");
const timer_head = document.getElementById("timer_head");
const timer = document.getElementById("timer");

var exerciseTime = 10;
var readyTime = 5;
var round = 1;
var cycle = 2;

var min = "";
var sec = "";

let startMode = false;
let intervalTime = "";

let isReady = true;
let isExcercise = false;

//준비시간 defualt
timer.innerHTML = "0" + ":" + checkTime(readyTime % 60);

function countReadyTimer() {
  intervalTime = setInterval(function () {
    min = parseInt(readyTime / 60);
    sec = readyTime % 60;

    timer.innerHTML = min + ":" + checkTime(sec);
    readyTime--;

    if (readyTime < 0) {
      stopTimer();

      isReady = false;
      start_btn.innerText = "시작";
      countExcerciseTimer();
    }
  }, 1000);
}

function countExcerciseTimer() {
  timer_head.innerHTML = "운동";
  isExcercise = true;

  intervalTime = setInterval(function () {
    min = parseInt(exerciseTime / 60);
    sec = exerciseTime % 60;

    timer.innerHTML = min + ":" + checkTime(sec);
    exerciseTime--;

    if (exerciseTime < 0) {
      stopTimer();

      isExcercise = false;
      start_btn.innerText = "시작";
    }
  }, 1000);
}

//타이머를 시작한다.
function startTimer() {
  startMode = true;
  if (isReady) {
    countReadyTimer();
  } else {
    countExcerciseTimer();
    // timer.innerHTML = "종료";
  }
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

// 현재시간 두자리수 맞추기
function checkTime(i) {
  if (i < 10) {
    i = "0" + i;
  }
  return i;
}
