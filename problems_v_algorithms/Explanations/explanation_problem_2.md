## Explanation

The way to accomplish this problem is to determine where the pivot point is for the rotated array, which we can do with a binary search.  Once this is determined, we can check if the number we are searching for is greater than the number at the 0th index.

If yes, we know that we can search only in the "left" half of the array.  If no, we can search in the "right" half of the array.  Then we do a simple binary search to find our number more quickly.

## Time complexity

We employ binary search twice in this problem, with a time complexity of O(log n).