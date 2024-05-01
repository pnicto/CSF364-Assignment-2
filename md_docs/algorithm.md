# Algorithm

## Problem Statement

The algorithm implemented as part of this assignment and also discussed in the class is from the book **Algorithm Design by Eva Tardos and Jon Kleinberg** and is given by **Ruth Nussinov**. The algorithm is used to compute the number of possible RNA pairs for a given RNA sequence. The algorithm is based on the concept of dynamic programming and uses a recursive approach to solve the problem. The base pairing follows the fundamental rules in biology i.e., **A** pairs with **U** and **G** pairs with **C**.

For a given RNA sequence, we say that a secondary structure is a list of pairs that satisfies the following conditions:

1. No sharp turns i.e., the ends of each pair in S are separated by at least four intervening bases.
2. The elements of any pair consist of either {A, U} or {C, G} (in either order).
3. No base pair appears more than once.
4. No crossing between pairs.

## Dynamic Programming Approach

Let the secondary structure of the given RNA sequence be denoted by \f$S\f$, where \f$S\f$ is a set of pairs \f$\{ (i, j) \}\f$ such that \f$1 \leq i , j \leq n\f$ and \f$n\f$ is the length of the RNA sequence. We say that \f$OPT(i, j)\f$ denotes the maximum number of base pairs in secondary structure of a sequence \f$b_i, b_{i+1}, \ldots, b_j\f$. The recursive formula for \f$OPT(i, j)\f$ is given by:

\f$OPT(i, j) = \biggl\{ \begin{array}{ll} 0 & \text{if } i \geq j-4 \\  max\{OPT(i, j-1), max_{\forall t} \{1 + OPT(i, t-1) + OPT(t+1, j-1)\}\} & \text {otherwise where } i \leq t < j-4 \end{array}\f$

Here \f$OPT(i,j-1)\f$ indicates the case where \f$j\f$ is not a member of any pair. If \f$j\f$ pairs with some \f$t < j - 4\f$, the knot condition yields two independent sub-problems \f$OPT(i, t-1)\f$ and \f$OPT(t+1, j-1)\f$.

## Time Complexity

The time complexity for this problem can be calculated as follows:

The number of sub-problems is \f$O(n^2)\f$ and evaluating the recurrence each of these problems takes \f$O(n)\f$ time. Hence, the total time complexity is \f$O(n^3)\f$.

## Other Algorithms

There are other dynamic programming solutions for this problem and they are more involved than the one discussed here. The algorithm implemented as part of this assignment does not focus on the energies of the pairs and hence is simpler. The other algorithms focus on the energies of the pairs. We list some of the algorithms here

-   McCaskill's Algorithm
-   Maximum Expected Accuracy (MEA) Algorithm

## Example Output

```plaintext
The pairs are:
{0 , 53} {1 , 8} {2 , 7} {9 , 52} {10 , 50} {11 , 49} {12 , 46} {13 , 45} {14 , 43} {17 , 41} {18 , 40} {19 , 39} {20 , 37} {21 , 36} {22 , 35} {23 , 28} {29 , 34}


In dot bracket notation:
(((....))((((((..(((((((....)(....)))).))).).))..)).))..
Total 17 pairs in the calculated RNA secondary structure
There are 13 pairs in the RNACentral result
There is a 50% match between the two results
```

<img
    src="example1.png"
    style="width: 100%;"
    />

## References

-   Kleinberg, J., & Tardos, E. (2022). Algorithm Design (2nd ed.). Pearson.
-   Raden, M., Mohamed, M. M., Ali, S. M., & Backofen, R. (2018). Interactive implementations of thermodynamics-based RNA structure and RNA-RNA interaction prediction approaches for example-driven teaching. PLOS Comput. Biol, 14(8), e1006341. doi:10.1371/journal.pcbi.1006341
-   Raden, M., Ali, S. M., Alkhnbashi, O. S., Busch, A., Costa, F., Davis, J. A., … Backofen, R. (2018). Freiburg RNA tools: a central online resource for RNA-focused research and teaching. Nucleic Acids Research, 46(W1), W25–W29. doi:10.1093/nar/gky329
-   Nussinov, R., Pieczenik, G., Griggs, J. R., & Kleitman, D. J. (1978). Algorithms for Loop Matchings. SIAM Journal on Applied Mathematics, 35(1), 68–82. doi:10.1137/0135006
