#!/usr/node
const args = process.arg;
const num = parseInt(args[2]);
if (isNaN(num)) {
	console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
     console.log('X'.repeat(num));
  }
}
