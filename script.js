// 자음/모음 리스트
const letters = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ", "ㅂ", "ㅅ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ", 
    "ㅏ", "ㅑ", "ㅓ", "ㅕ", "ㅗ", "ㅛ", "ㅜ", "ㅠ", "ㅡ", "ㅣ"];

// HTML 요소 참조
const randomContainer = document.getElementById("random-container");
const newLetterButton = document.getElementById("new-letter-button");

// 랜덤 이미지와 사운드 표시 함수
function displayRandomLetter() {
// 컨테이너 초기화 (기존 이미지 제거)
randomContainer.innerHTML = "";

// 랜덤으로 하나의 자음/모음 선택
const randomLetter = letters[Math.floor(Math.random() * letters.length)];

// 이미지와 데이터 속성 추가
const letterDiv = document.createElement("div");
letterDiv.classList.add("letter");
letterDiv.setAttribute("data-sound", randomLetter);

const img = document.createElement("img");
img.src = `assets/images/${randomLetter}.png`;
img.alt = randomLetter;

// 이미지 클릭 시 사운드 재생 이벤트 추가
letterDiv.addEventListener("click", () => {
const audio = new Audio(`assets/sounds/${randomLetter}.mp3`);
audio.play();
});

// DOM에 추가
letterDiv.appendChild(img);
randomContainer.appendChild(letterDiv);
}

// 초기 랜덤 이미지 표시
displayRandomLetter();

// 버튼 클릭 시 새로운 랜덤 이미지 표시
newLetterButton.addEventListener("click", displayRandomLetter);