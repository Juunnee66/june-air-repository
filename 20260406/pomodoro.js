const timeInput = document.querySelector("#time-input");
const startBtn = document.querySelector("#start-timer");
const stopBtn = document.querySelector("#stop-timer");
const display = document.querySelector("#timer-display");

let timerId = null;
let remainingSeconds = 0;

// 초 -> 분으로표시
function updateDisplay() {
    const min = Math.floor(remainingSeconds / 60);
    const sec = remainingSeconds % 60; // 60으로 나눈 나머지는 초

    //1:3 -> 01:03 -> 앞자리에0넣어줌
    display.textContent = 
        String(min).padStart(2, "0") + ":" + String(sec).padStart(2, "0");
    display.className = "fs-3";
}

// timer 시작
startBtn.addEventListener("click", () => {
    // 이미 타이머가 동작중이면, 다음 실행 무시
    if (timerId !== null){
        // alert("이미 실행중인 타이머가 있습니다"); -> alert 뜨면 기존 타이머가 진행이안됨
        return;
    };

    // 분단위, 숫자만 입력값으로 받음
    const minutes = Number(timeInput.value); 
    if (!minutes || isNaN(minutes) || minutes <= 0 ) {
        alert ("시간을 숫자로만(분단위) 입력하세요");
        return;
    };
    
    remainingSeconds = minutes*60;
    updateDisplay();

    // 1초마다 반복적으로 동작하는 함수 추가
    timerId = setInterval(() => {
        remainingSeconds--;

        // 0초가 되면 타미머 종료
        if (remainingSeconds <= 0) {
            resetTimer();
        } else {
            updateDisplay();
        };
    }, 1000);
});

// 타이머 중지
stopBtn.addEventListener("click", resetTimer);

function resetTimer() {
    clearInterval(timerId);
    timerId = null;
};