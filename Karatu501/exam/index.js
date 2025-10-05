let hours = 0;
let minutes = 0;
let seconds = 0;
let milliseconds = 0;
let timer = null;
let isRunning = false;

const display = document.getElementById("watch");
const startButton = document.getElementById("start");
const stopButton = document.getElementById("stop");
const resetButton = document.getElementById("reset");

function displayTime() {
  let hr = hours < 10 ? "0" + hours : hours;
  let min = minutes < 10 ? "0" + minutes : minutes;
  let sec = seconds < 10 ? "0" + seconds : seconds;
  let ms = Math.floor(milliseconds / 10)
    .toString()
    .padStart(2, "0");

  display.innerText = `${hr}:${min}:${sec}:${ms}`;
}

function startTime() {
  if (!isRunning) {
    isRunning = true;
    timer = setInterval(() => {
      milliseconds += 10;
      if (milliseconds === 1000) {
        milliseconds = 0;
        seconds++;
      }
      if (seconds === 60) {
        seconds = 0;
        minutes++;
      }
      if (minutes === 60) {
        minutes = 0;
        hours++;
      }
      displayTime();
    }, 10);
  }
}

function stopTime() {
  clearInterval(timer);
  isRunning = false;
}

function resetTime() {
  clearInterval(timer);
  isRunning = false;
  hours = 0;
  minutes = 0;
  seconds = 0;
  milliseconds = 0;
  displayTime();
}

startButton.addEventListener("click", startTime);
stopButton.addEventListener("click", stopTime);
resetButton.addEventListener("click", resetTime);