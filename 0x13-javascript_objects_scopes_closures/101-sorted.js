#!/usr/bin/node
const dict = require('./101-data').dict;
const sortedDict = {};
for (const prop of Object.values(dict)) sortedDict[prop] = [];
for (const [key, prop] of Object.entries(dict)) sortedDict[prop].push(key);
console.log(sortedDict);
