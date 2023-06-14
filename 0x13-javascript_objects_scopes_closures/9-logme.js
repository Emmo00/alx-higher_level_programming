#!/usr/bin/node
let _nb = 0;
exports.logMe = function (item) {
  console.log(`${_nb++}: ${item}`);
};
