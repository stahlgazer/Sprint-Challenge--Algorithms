#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) because calculations are based directly with the size of n.


b) O(n log n) or something similar because while operations increase with n, j is multiplied by 2 which decreases the amount of calculations needed in half for the 2nd loop.


c) O(n) or something simliar because the size of input directly affects how many recursions take place.

## Exercise II

I would probably use binary search to reduce the amount of guesses needed.
First find the middle floor of n, check if egg breaks or not, if it doesn't then remove bottom half and keep moving higher with the new middle. If egg breaks, remove top half and go lower, since we need to find the floor it breaks on. Would be O(log n) since it's linear but halving with each calculation.
