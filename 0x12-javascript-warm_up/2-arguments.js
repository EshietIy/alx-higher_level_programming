#!/usr/bin/node
let args = process.argv.slice(2);
if (args.length === 0){
  console.log('No argument');
} else {
  console.log('Arguments found');
}
