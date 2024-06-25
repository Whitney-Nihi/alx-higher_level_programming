#!/usr/bin/node
// Creates a sentence with two arguments passed to it

if (process.argv[2] && process.argv[3]) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
} else if (process.argv[2]) {
  console.log(process.argv[2] + ' is ' + undefined);
} else {
  console.log(undefined + ' is ' + undefined);
}
