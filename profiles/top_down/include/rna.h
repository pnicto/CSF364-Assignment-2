/**
 * @file rna.h
 * @brief Contains the declaration of RNA class.
 *
 */
#ifndef RNA_H
#define RNA_H

#include <algorithm>
#include <iostream>
#include <fstream>
#include <stack>
#include <vector>

using namespace std;

/**
 * @brief A class that represents a RNA sequence.
 *
 */
class RNA
{
public:
    /**
     * @brief Construct a new RNA object.
     *
     * @param s The input RNA sequence.
     */
    explicit RNA(string s, string d = "");
    /**
     * @brief Prints pairings in the secondary structure.
     *
     */
    void printPairs() const;

private:
    /**
     * @brief Checks if the RNA sequence is valid i.e. made up of A,U,G or C nucleotides.
     *
     * @return true If valid.
     * @return false If invalid.
     */
    bool validate();
    /**
     * @brief Checks if two given nucleotides can be paired up.
     *
     * @param a A nucleotide.
     * @param b A nucleotide.
     * @return true If they can be paired up.
     * @return false If they cannot be paired up.
     */
    bool match(char a, char b) const;
    /**
     * @brief Calculates maximum number of pairs in the RNA sequence.
     *
     * @param s The RNA sequence.
     * @param l The left index.
     * @param r The right index.
     */
    int numOfPairs(const string &s, int l, int r);
    /**
     * @brief Computes pairs in the RNA sequence.
     *
     * @param l The left index.
     * @param r The right index.
     */
    void computePairs(int l, int r);
    /**
     * @brief Generates a corresponding dot bracket notation for pairs.
     *
     */
    void genDotBracketResult();
    /**
     * @brief Compares the algorithmic result with the actual result/secondary structure.
     *
     */
    void compare() const;

    /**
     * @brief Holds the input RNA sequence.
     *
     */
    string sequence;
    /**
     * @brief Holds the dot bracket representation of the given/real RNA structure.
     *
     */
    string dotBracketInput;
    /**
     * @brief Holds the dot bracket representation of pairs computed by the algorithm.
     *
     */
    string dotBracketResult;
    /**
     * @brief Holds the length of the RNA sequence.
     *
     */
    int length;
    /**
     * @brief Holds the result of RNA::validate() .
     *
     */
    bool valid;
    /**
     * @brief Two dimensional array used for bottom up dynamic programming in RNA::numOfPairs() .
     *
     */
    vector<vector<int>> dp;
    /**
     * @brief Two dimensional array used for calculating pairs in RNA::computePairs() .
     *
     */
    vector<vector<int>> jPairs;
    /**
     * @brief Holds the nucleotide pairs in the RNA sequence.
     *
     */
    vector<pair<int, int>> pairs;
};

#endif // RNA_H