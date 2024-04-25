# Algorithm

## Problem Statement

The algorithm implemented as part of this assignment and also discussed in the class is from the book **Algorithm Design by Eva Tardos and Jon Kleinberg**. The algorithm is used to compute the number of possible RNA pairs for a given RNA sequence. The algorithm is based on the concept of dynamic programming and uses a recursive approach to solve the problem. The base pairing follows the fundamental rules in biology i.e., **A** pairs with **U** and **G** pairs with **C**.

For a given RNA sequence, we say that a secondary structure is a list of pairs that satisfies the following conditions:

1. No sharp turns i.e., the ends of each pair in S are separated by at least four intervening bases.
2. The elements of any pair consist of either {A, U} or {C, G} (in either order).
3. No base pair appears more than once.
4. No crossing between pairs.

## Dynamic Programming Approach

Let the secondary structure of the given RNA sequence be denoted by \f$S\f$, where \f$S\f$ is a set of pairs \f$\{ (i, j) \}\f$ such that \f$1 \leq i , j \leq n\f$ and \f$n\f$ is the length of the RNA sequence. We say that \f$OPT(i, j)\f$ denotes the maximum number of base pairs in secondary structure of a sequence \f$b_i, b_{i+1}, \ldots, b_j\f$. The recursive formula for \f$OPT(i, j)\f$ is given by:

\f$OPT(i, j) = \biggl\{ \begin{array}{ll} 0 & \text{if } i \geq j-4 \\  max\{OPT(i, j-1), max\{1 + OPT(i, t-1) + OPT(t+1, j-1)\}\} & \text {otherwise where } i \leq t < j-4 \end{array}\f$

Here \f$OPT(i,j-1)\f$ indicates the case where \f$j\f$ is not a member of any pair. If \f$j\f$ pairs with some \f$t < j - 4\f$, the knot condition yields two independent sub-problems \f$OPT(i, t-1)\f$ and \f$OPT(t+1, j-1)\f$.

## Time Complexity

The time complexity for this problem can be calculated as follows:

The number of sub-problems is \f$O(n^2)\f$ and evaluating the recurrence each of these problems takes \f$O(n)\f$ time. Hence, the total time complexity is \f$O(n^3)\f$.
