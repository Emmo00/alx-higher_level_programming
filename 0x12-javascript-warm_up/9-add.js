#!/usr/bin/node
let a = Number(process.argv[2])
let b = Number(process.argv[3])
function add(a, b) {
  return a + b
}
console.log(add(a, b))
