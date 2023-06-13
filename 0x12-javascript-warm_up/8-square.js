#!/usr/bin/node
let squareSize = Number(process.argv[2])
if (Number.isNaN(squareSize)) {
    console.log('Missing size')
    return
}
for (let i = 0; i < squareSize; i++) {
    let row = ''
    for (let j = 0; j < squareSize; j++) {
        row = row.concat('X')
    }
    console.log(row);
}
