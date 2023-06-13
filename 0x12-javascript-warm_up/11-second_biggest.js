#!/usr/bin/node
let arguments = process.argv.slice(2)
function secondBiggest(arr) {
  arr = arr.map((a) => Number(a))
  if (arr.length <= 1) return 0
  let max = Math.max(...arr)
  arr = arr.filter((elem) => elem !== max)
  return Math.max(...arr)
}
console.log(secondBiggest(arguments))
