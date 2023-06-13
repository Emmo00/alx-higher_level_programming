#!/usr/bin/node
const timesToPrint = Number(process.argv[2]);
if (Number.isNaN(timesToPrint)) {
  console.log('Missing number of occurrences');
  process.exit();
}
for (let i = 0; i < timesToPrint; i++) {
  console.log('C is fun');
}
