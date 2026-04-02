// (기본) 함수를 선언한 곳에서 직접 호출
// (응용) 함수를 선언한 곳과 호출하는 곳이 다름
// 함수 값처럼 다루기
// 함수를 변수에 할당하기

//함수 정의
function sayHello() {
    console.log("Hello!");
};

//함수 호출
sayHello(); // Hello!

//함수
console.log(sayHello);

//변수에 할당하기
const f = sayHello;
console.log(f);

// 함수를 다른 함수의 인자(변수)로 전달하기
function run(fn) {
    console.log("start function run...")
    fn();
    console.log("end function run...")
}

run(sayHello)
// run(sayHello())->이경우는 sayHello를 호출한다음에 넣은거라 return값이 들어가게됨-> undefined가 들어감

