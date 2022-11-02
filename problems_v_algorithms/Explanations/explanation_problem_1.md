## Explanation

For this problem, I learned that there are several mathematical assumptions which we can employ.  For example, we can assume that the square root of a number will be less than half of that number.

From there, we can employ a binary search to more quickly get to our answer.

## Time complexity

The time complexity of a binary search is O(log n).

## Space complexity

While we are creating an upper bound by taking half of the number input, we are not creating a data structure with all the numbers up to that input, rather doing mathematical calculations.  Space complexity stays constant, O(1).