
## Wordle solver

Upon starting this script you are prompted to enter a string of letters and numbers, and a pipe.

Everything left of the pipe is "positive" meaning it indicates a letter used in the wordle; everything right of the pipe is "negative."

Capital letters followed by a number to indicate that letter is in that position. E.g. `Z5` means the `5th` character is `z`

The digits following a lower-case letter indicate positions that letter is NOT in, but implies that the letter IS used in that word. E.g. 'b234' means `b` _IS_ used in this word, but is not in the 2nd, 3rd, or 4th position (may be in 1st or 5th)

All letters following a pipe `|` are rejected letters

Full example: `Z5b234|efg` means `Z` is the 5th letter; `b` is in the word but not the 2nd, 3rd, or 4th letter; and the letters `e`, `f`, and `g` are _not_ in the word.

You can enter just a pipe `|` to display ALL ranked matches. Just press enter (with no input) to exit, or CTRL+C.

This script is not stupid-proof and was created mostly as a PoC.

In the Wordle game I play, not all words in my dictionary (the 5\_letter\_words.txt file) work, but you are not punished for guessing those words.
