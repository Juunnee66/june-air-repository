// 지금까지배운걸 활용하여 실습하기
// 조건문, 반복문, 함수 등

function getAverage(scores) {
    // 평균 = 총합/갯수
    // 갯수 = scores.length
    // 총합 = 반복문으로 더하기
    
    // 오류 걸러주기(array가 비었을경우)
    if (scores.length === 0) {
        return 0;
    };

    let sum = 0
    for (const score of scores) {
        sum += score
    };
    return sum/scores.length;
};


const scores = [80, 85, 92, 97]
const average = getAverage(scores)
console.log(average)