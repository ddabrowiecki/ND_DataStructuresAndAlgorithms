## Explanation

In this problem, we can also employ some mathematical assumptions.  To get the integers that make the biggest sum, we want to concatenate the integers from largest to smallest, but alternating.  

We loop through the array, finding the maximum integer and then remove it from the array.  We accomplish the alternation by selecting even indices (which change as we subtract an element after finding the maximum).

## Time complexity

The solution runs in linear time, O(n).