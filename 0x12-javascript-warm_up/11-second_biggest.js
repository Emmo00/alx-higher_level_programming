#!/usr/bin/node
const args = process.argv.slice(2);
function secondBiggest (arr) {
  arr = arr.map((a) => Number(a));
  if (arr.length <= 1) return 0;
  const max = Math.max(...arr);
  arr = arr.filter((elem) => elem !== max);
  return Math.max(...arr);
}
console.log(secondBiggest(args));
