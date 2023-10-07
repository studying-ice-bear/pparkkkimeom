// https://www.acmicpc.net/problem/1182
const fs = require("fs");
const path = require("path");
const problemID = path.basename(__filename).split("_")[0];
let fileLocation =
  process.platform === "darwin" ? `./${problemID}.txt` : "/dev/stdin";
const testCasePath = path.resolve(__dirname, fileLocation);

const [NS, num] = fs.readFileSync(testCasePath).toString().trim().split("\n");

const [N, S] = NS.split(" ").map((ele) => +ele);
const numArr = num.split(" ").map((ele) => +ele);

// 메모리 초과
// let answer = 0;

// const getCombination = (arr, count) => {
//   if (count === 1) return arr.map((ele) => [ele]);
//   const result = [];
//   arr.forEach((fixed, idx) => {
//     const rest = arr.slice(idx + 1);
//     const combination = getCombination(rest, count - 1);
//     const attached = combination.map((combi) => [fixed, ...combi]);
//     result.push(...attached);
//   });
//   return result;
// };

// for (let i = 1; i <= N; i++) {
//   const combiArrByCount = getCombination(numArr, i);
//   combiArrByCount.forEach((ele) => {
//     if (ele.reduce((a, b) => a + b, 0) === S) {
//       answer++;
//     }
//   });
// }
// console.log(answer);

let answer = 0;

const add = (curr, total) => {
  if (curr === N) {
    if (total === S) answer++;
    return;
  }
  add(curr + 1, total);
  add(curr + 1, total + numArr[curr]);
};

add(0, 0);

if (S === 0) answer--;
console.log(answer);
