## Explanation

For this problem, we implement a trie, creating a class with insert and find methods.  We then use these methods for our Router class.

## Time complexity

The time complexity of this solution requires that we take into account the number of paths
included (n) as well as the average length of the paths (L), in big O notation: O(n*L).

## Space complexity

Our data structure may need to save many paths, which may share parent paths.  Also, we need to factor in the number of children a node can have, based on the number of valid paths we are using.

Space complexity is O(a * L * n), factoring in alphabet length (a), average length of word (L) and number of valid paths.