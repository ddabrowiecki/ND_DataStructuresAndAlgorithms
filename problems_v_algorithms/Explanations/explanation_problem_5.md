## Explanation

For this problem, we implemented a trie, using recursion to recursively capture suffixes of words saved in the trie.

## Time complexity

The time complexity of this solution requires that we take into account the number of words
included (n) as well as the average length of the word (L), in big O notation: O(n*L).

## Space complexity

Our data structure may need to save many long words, which may share characters or not.  Also, we need to factor in the number of children a node can have, based on the number of characters in the alphabet we are using.

Space complexity is O(a * L * n), factoring in alphabet length (a), average length of word (L) and number of words.