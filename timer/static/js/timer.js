const start_btn = document.getElementById("start_btn");
const timer_head = document.getElementById("timer_head");
const timer = document.getElementById("timer");
const totalTimer_head = document.getElementById("totalTime");
const timer_head_next = document.getElementById("timer_head_next");
const timer_next = document.getElementById("timer_next");
const round_cnt = document.getElementById("round_cnt");
const cycle_cnt = document.getElementById("cycle_cnt");

var exerciseTime = 5;
var readyTime = 2;
var breakTime = 3;
var round = 2;
var cycle = 2;
var cycleBreakTime = 4;

var leftRound = 0;
var totalTime = 0;
var defaultTotalTime = 0;
var defualtRound = round;
var defaultCylce = cycle;

var min = "";
var sec = "";

let startMode = false;

let isReady = true;
let isExcercise = false;
let isBreak = false;
let isCycleBreak = false;

var timerQueueArray = ["r"];

//저장된 운동 리스트와 시간을 불러온다.

//운동순서와 총 운동시간을 셋팅한다.
for (i = 0; i < cycle; i++) {
  for (j = 0; j < round; j++) {
    timerQueueArray.push("e");
    totalTime += exerciseTime;
    //마지막 라운드에는 휴식시간이 없음.
    if (j < round - 1) {
      timerQueueArray.push("b");
      totalTime += readyTime;
    }
  }
  //마지막 사이클에는 휴식시간이 없음.
  if (i < cycle - 1) {
    timerQueueArray.push("bc");
    totalTime += cycleBreakTime;
  }
  defaultTotalTime = totalTime;
  console.log(timerQueueArray);
}

//준비시간 defualt fizme
timer.innerHTML = formatTwoDigits(readyTime);
timer_next.innerHTML = formatTwoDigits(exerciseTime);
round_cnt.innerHTML = round;
cycle_cnt.innerHTML = cycle;
timer_head_next.innerHTML = "운동";
//전체시간 defulat
totalTimer_head.innerHTML = formatTwoDigits(totalTime);
function formatTwoDigitsMin(n) {
  var m = parseInt(n / 60);
  return (m < 10 ? "0" : "") + m;
}

function formatTwoDigitsSec(n) {
  var s = n % 60;
  return (s < 10 ? "0" : "") + s;
}

//시간을 두자리수로 맞춘다.
function formatTwoDigits(n) {
  var m = parseInt(n / 60);
  var s = parseInt(n % 60);

  return (m < 10 ? "0" : "") + m + ":" + (s < 10 ? "0" : "") + s;
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

//타이머를 시작한다.
function startTimer() {
  startMode = true;
  if (leftRound < timerQueueArray.length) {
    if (isReady) {
      console.log("ready ");

      var newTime = readyTime;
      timer_head.innerHTML = "준비";
      timer.innerHTML = formatTwoDigits(newTime);

      readyInterval = setInterval(function () {
        isReady = true;

        newTime--;
        totalTime--;

        totalTimer_head.innerHTML = formatTwoDigits(totalTime);
        timer.innerHTML = formatTwoDigits(newTime);

        if (newTime === 1) {
          stopTimer();
          isReady = false;

          //라운드 추가
          leftRound++;

          loopTimer();
        }
      }, 1000);
    } else if (isExcercise) {
      console.log("운동이삼 ");
      timer_head.innerHTML = "운동";
      var newTime = exerciseTime;
      timer.innerHTML = formatTwoDigits(newTime);

      ExcerciseInterval = setInterval(function () {
        isExcercise = true;
        newTime--;
        totalTime--;

        totalTimer_head.innerHTML = formatTwoDigits(totalTime);
        timer.innerHTML = formatTwoDigits(newTime);
        if (newTime === 1) {
          stopTimer();
          isExcercise = false;

          //라운드 추가
          leftRound++;
          round--;
          round_cnt.innerHTML = round;

          loopTimer();
        }
      }, 1000);
    } else if (isBreak) {
      console.log("휴식이삼 ");
      var newTime = breakTime;

      timer_head.innerHTML = "휴식";
      timer.innerHTML = formatTwoDigits(newTime);

      breakInterval = setInterval(function () {
        isBreak = true;
        newTime--;
        totalTime--;

        totalTimer_head.innerHTML = formatTwoDigits(totalTime);

        timer.innerHTML = formatTwoDigits(newTime);
        if (newTime === 1) {
          stopTimer();
          isBreak = false;

          //라운드 추가
          leftRound++;
          loopTimer();
        }
      }, 1000);
    } else if (isCycleBreak) {
      console.log("사이클휴식이삼 ");
      var newTime = cycleBreakTime;

      timer_head.innerHTML = "사이클휴식 ";
      timer.innerHTML = formatTwoDigits(newTime);
      //사이클 휴식때는 round refresh;
      round = defualtRound;
      cycleBreakInterval = setInterval(function () {
        isCycleBreak = true;
        newTime--;
        totalTime--;

        totalTimer_head.innerHTML = formatTwoDigits(totalTime);
        timer.innerHTML = formatTwoDigits(newTime);
        if (newTime === 1) {
          stopTimer();
          isCycleBreak = false;

          //라운드 추가
          leftRound++;
          round_cnt.innerHTML = round;

          cycle--;
          cycle_cnt.innerHTML = cycle;
          loopTimer();
        }
      }, 1000);
    }
  } else {
    refreshTimer();
  }
}

//타이머를 멈춘다.
function stopTimer() {
  startMode = false;
  if (isReady) {
    clearInterval(readyInterval);
  } else if (isExcercise) {
    clearInterval(ExcerciseInterval);
  } else if (isBreak) {
    clearInterval(breakInterval);
  } else if (isCycleBreak) {
    clearInterval(cycleBreakInterval);
  }
}

// //화면을 전환한다.
// function changeScreen(v) {}

function parseTime(time) {
  var time = time.split(":");
  var SECONDS = parseInt(time[1]);
  var MINUTES = parseInt(time[0]);
  return [MINUTES, SECONDS];
}

//시간을 변경한다. 1초 delay 삭제
function changeTime(cur, deltaTime) {
  var time = parseInt(cur);
  var minutes = parseInt(time / 60);
  var seconds = parseInt(time % 60);

  console.log(minutes, seconds);
  var newTime = 0;

  if (seconds === 59 && deltaTime === "+1") {
    newTime = (minutes + 1) * 60;
  } else if (minutes >= 1 && seconds === 0 && deltaTime === "-1") {
    newTime = (minutes - 1) * 60 + 59;
  } else if (minutes === 0 && seconds === 0 && deltaTime === "-1") {
    newTime = minutes * 60 + seconds;
  } else {
    var tempTime = seconds + parseInt(deltaTime);
    newTime = minutes * 60 + tempTime;
  }
  console.log(newTime);
  return newTime;
}

function loopTimer() {
  console.log(leftRound, "leftround");
  //라운드횟수가 토탈 라운드보다 커지면 루프 그만.
  if (leftRound <= timerQueueArray.length) {
    if (timerQueueArray[leftRound] === "e") {
      isExcercise = true;
    } else if (timerQueueArray[leftRound] === "b") {
      isBreak = true;
    } else if (timerQueueArray[leftRound] === "bc") {
      isCycleBreak = true;
    }

    startTimer();
    nextRound();
  }
}

//다음 운동을 셋팅한다.
function nextRound() {
  if (leftRound < timerQueueArray.length) {
    if (timerQueueArray[leftRound + 1] === "e") {
      timer_head_next.innerHTML = "운동";
      timer_next.innerHTML = formatTwoDigits(exerciseTime);
    } else if (timerQueueArray[leftRound + 1] === "b") {
      timer_head_next.innerHTML = "휴식";
      timer_next.innerHTML = formatTwoDigits(breakTime);
    } else if (timerQueueArray[leftRound + 1] === "bc") {
      timer_head_next.innerHTML = "사이클휴식";
      timer_next.innerHTML = formatTwoDigits(cycleBreakTime);
    }
  } else {
    refreshTimer();
  }
}

//타이머를 리프레시 한다.
function refreshTimer() {
  startMode = false;
  start_btn.innerText = "시작";

  //준비시간 defualt fizme
  timer_head_next.innerHTML = "운동";
  timer_head.innerHTML = "준비";
  timer.innerHTML = formatTwoDigits(readyTime);
  timer_next.innerHTML = formatTwoDigits(exerciseTime);

  //전체시간 defulat
  totalTimer_head.innerHTML = formatTwoDigits(defaultTotalTime);
  totalTime = defaultTotalTime;
  round = defualtRound;
  round_cnt.innerHTML = round;
  leftRound = 0;

  cycle = defaultCylce;
  cycle_cnt.innerHTML = cycle;

  isReady = true;
}
