#!/usr/bin/node
const fs = require('fs');
const [fileA, fileB, outputFile] = process.argv.slice(2);
let textBuffer = '';
textBuffer = fs.readFileSync(fileA, { encoding: 'utf8' });
textBuffer += fs.readFileSync(fileB, { encoding: 'utf8' });
fs.writeFileSync(outputFile, textBuffer);
