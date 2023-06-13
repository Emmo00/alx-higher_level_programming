#!/usr/bin/node
let arguments = process.argv.slice(2)
function secondBiggest(arr) {
  let max = Math.max()
  let secondBiggest
  if (arr.length <= 1) return 0
  for (let i of arr) {
    if (!secondBiggest) secondBiggest = i
    if (i < max && i > secondBiggest) secondBiggest = i
  }
  return secondBiggest
}
console.log(secondBiggest(arguments))
