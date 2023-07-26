#!/usr/bin/node
const request = require('request')
const response = request.get(process.argv[2])
response.on('complete', (res) => {
	console.log(res.statusCode)
})