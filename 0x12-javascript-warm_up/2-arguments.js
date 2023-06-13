#!/usr/bin/node
const argumentLength = process.argv.length;
if (argumentLength <= 2) {
  console.log('No argument');
} else if (argumentLength === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
