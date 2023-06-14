// https://www.acmicpc.net/problem/2630
const [n, ...arr] = require("fs").readFileSync("/dev/stdin").toString().trim().split(/\n/);

const paperInfo = arr.map((row) => row.split(" "));

let [totalWhiteCount, totalBlueCount] = [0, 0];

const isOnePaper = (arr) => {
  let [whiteCount, blueCount] = [0, 0];
  let isOne = true;
  arr.forEach((row) => {
    row.forEach((ele) => {
      ele === "0" ? whiteCount++ : blueCount++;
      if (whiteCount * blueCount !== 0) {
        isOne = false;
        return false;
      }
    });
    if (!isOne) return false;
  });
  return isOne;
};

const cutQuarter = (arr) => {
  const sideLength = arr.length;
  if (sideLength == 2) {
    if (isOnePaper(arr)) {
      arr[0][0] === "0" ? (totalWhiteCount += 1) : (totalBlueCount += 1);
    } else {
      arr.map((row) =>
        row.map((ele) => (ele === "0" ? (totalWhiteCount += 1) : (totalBlueCount += 1)))
      );
    }
    return false;
  }
  if (isOnePaper(arr)) {
    arr[0][0] === "0" ? (totalWhiteCount += 1) : (totalBlueCount += 1);
    return false;
  }
  const [start, end] = [
    [0, sideLength / 2],
    [sideLength / 2, sideLength],
  ];
  const result = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1],
  ].map((idx) => {
    let [startIdx, endIdx] = idx;
    let eachQuarter = [];
    for (let i = start[startIdx]; i < end[startIdx]; i++) {
      let row = [];
      for (let j = start[endIdx]; j < end[endIdx]; j++) {
        row.push(arr[i][j]);
      }
      eachQuarter.push(row);
    }
    return eachQuarter;
  });
  result.map((ele) => cutQuarter(ele));
};

cutQuarter(paperInfo);
console.log(totalWhiteCount);
console.log(totalBlueCount);
