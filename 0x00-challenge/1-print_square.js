#!/usr/bin/node
/*
    Print a square with the character #

    The size of the square must be the first argument
    of the program.
*/

if (process.argv.length <= 2) {
  process.stderr.write('Missing argument\n');
  process.stderr.write('Usage: ./1-print_square.js <squareSize>\n');
  process.stderr.write('Example: ./1-print_square.js 8\n');
  process.exit(1);
}

const squareSize = parseInt(process.argv[2], 10);

for (let row = 0; row < squareSize; row++) {
  for (let col = 0; col < squareSize; col++) {
    process.stdout.write('#');
  }
  process.stdout.write('\n');
}
