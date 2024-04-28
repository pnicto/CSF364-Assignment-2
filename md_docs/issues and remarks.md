# Issues

## Algorithm Design

The algorithm/method `numOfPairs()` (by Eva Tardos and Jon Kleinberg) described in class does not compute RNA pairs, it just counts them. So, we had to modify the algorithm to save pair choices at every stage. Subsequently we compute pairs with `computePairs()` using these choices in a recursive manner. This does not increase the complexity because `computePairs()` is run after `numOfPairs()`, and as they share a similar recursive structure, `computePairs()` has no repeating subproblems as the solution for each subproblem is already memoized by `numOfPairs()` in the shared array `jPairs`.

## Visualization

## Buggy RNA on rnacentral.org

1. Some RNA on https://rnacentral.org is buggy and corrupt. For example: 
This RNA https://rnacentral.org/rna/URS0000ABD8B3/9606 has a rogue character `N` appearing in the sequence.
2. The dot bracket notational secondary structure is invalid sometimes due to (a) parenthetical sequence being invalid (due to mismatching parenthesis) or (b) length being different from initial RNA sequence.

# Remarks