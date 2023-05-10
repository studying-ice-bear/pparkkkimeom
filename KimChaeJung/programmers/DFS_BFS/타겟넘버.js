function solution(numbers, target) {
  var answer = 0;
  possibleNumbers = [];
  numbers.forEach((ele, idx) => {
    if (idx === 0) {
      possibleNumbers.push(ele);
      possibleNumbers.push(-ele);
    } else {
      let prevList = possibleNumbers.slice();
      let newResult = [];
      prevList.forEach((prevEle) => {
        newResult.push(prevEle + ele);
        newResult.push(prevEle - ele);
      });
      possibleNumbers = newResult;
    }
  });
  possibleNumbers.forEach((ele) => {
    if (ele === target) {
      answer += 1;
    }
  });
  return answer;
}
