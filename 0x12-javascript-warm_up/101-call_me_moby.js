#!/usr/bin/node
function callMeMoby (n, callback) {
  for (let i = 0; i < n; i++) callback();
}
module.exports = { callMeMoby };
