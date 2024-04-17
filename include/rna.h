#ifndef RNA_H
#define RNA_H

#include <iostream>
#include <vector>

using namespace std;

class RNA
{
public:
    explicit RNA(string s);
    void printPairs() const;

private:
    bool validate();
    bool match(char a, char b) const;
    void numOfPairs(const string &s, int l, int r);
    void computePairs(int l, int r);
    void genDotBracketResult();

    string sequence, dotBracketResult;
    int length;
    bool valid;
    vector<vector<int>> dp, jPairs;
    vector<pair<int, int>> pairs;
};

#endif // RNA_H