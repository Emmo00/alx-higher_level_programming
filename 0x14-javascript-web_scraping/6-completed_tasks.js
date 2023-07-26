#!/usr/bin/node
const request = require('request');
const apiURL = process.argv[2];

request.get(apiURL, {}, (err, res, data) => {
  if (err) console.log(err);
  tasks = JSON.parse(data);
  const usersCompleted = {};
  for (const task of tasks) {
    if (usersCompleted[task.userId] && task.completed) {
      usersCompleted[task.userId] += 1;
    } else if (!usersCompleted[task.userId] && task.completed) {
      usersCompleted[task.userId] = 1;
    }
  }
  console.log(usersCompleted);
});
