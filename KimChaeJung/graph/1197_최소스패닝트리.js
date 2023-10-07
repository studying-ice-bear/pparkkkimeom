// https://www.acmicpc.net/problem/1197
const fs = require("fs");
const [VE, ...arr] = fs.readFileSync("KimChaeJung/graph/1197.txt").toString().trim().split("\n");
// const [VE, ...arr] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [V, E] = VE.split(" ").map((ele) => +ele);
const edgeArr = arr.map((ele) => ele.split(" ").map((number) => +number));

let parent = Array.from({ length: V + 1 }, (_, idx) => idx);
let result = 0;

edgeArr.sort((a, b) => a[2] - b[2]);

const findParent = (x) => {
  if (parent[x] != x) parent[x] = findParent(parent[x]);
  return parent[x];
};

const unionParent = (a, b) => {
  a = findParent(a);
  b = findParent(b);
  if (a < b) parent[b] = a;
  else parent[a] = b;
};

for (const [a, b, cost] of edgeArr) {
  if (findParent(a) != findParent(b)) {
    unionParent(a, b);
    result += cost;
  }
}

console.log(result);

// 참고) 메모리 초과 나는 Prim 알고리즘
```
const fs = require("fs");
const [VE, ...arr] = fs.readFileSync("KimChaeJung/graph/1197.txt").toString().trim().split("\n");
// const [VE, ...arr] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const MAX = Number.MAX_SAFE_INTEGER;

const [V, E] = VE.split(" ").map((ele) => +ele);
const edgeArr = arr.map((ele) => ele.split(" "));
// const graph = Array.from({ length: V }, () => new Array(V).fill(0));
const graphInfo = new Array(V).fill(null).map(() => new Array(V).fill(MAX));

edgeArr.forEach(([A, B, C]) => {
  graphInfo[A - 1][B - 1] = +C;
  graphInfo[B - 1][A - 1] = +C;
});

for (let i = 0; i < V; i++) {
  graphInfo[i][i] = 0;
}

const minKey = (key, mstSet) => {
  let min = MAX;
  let minIdx;
  for (let vertex = 0; vertex < V; vertex++) {
    if (!mstSet[vertex] && key[vertex] < min) {
      min = key[vertex];
      minIdx = vertex;
    }
  }
  return minIdx;
};

const primMST = (graph) => {
  let parent = [];
  let key = Array(V).fill(MAX);
  let mstSet = Array(V).fill(false);

  key[0] = 0;
  parent[0] = -1;

  for (let count = 0; count < V - 1; count++) {
    let u = minKey(key, mstSet);
    mstSet[u] = true;
    for (let vertex = 0; vertex < V; vertex++) {
      if (graph[u][vertex] && !mstSet[vertex] && graph[u][vertex] < key[vertex]) {
        parent[vertex] = u;
        key[vertex] = graph[u][vertex];
      }
    }
  }

  let minWeight = 0;
  for (let i = 1; i < V; i++) {
    minWeight += graph[i][parent[i]];
  }
  return minWeight;
};

console.log(primMST(graphInfo));
```;
