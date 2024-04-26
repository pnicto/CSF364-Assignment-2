#ifndef RNA_H
#define RNA_H

#include <algorithm>
#include <iostream>
#include <fstream>
#include <stack>
#include <vector>

using namespace std;

class ProfileRNA
{
public:
    explicit ProfileRNA(string s);
    void printPairs() const;

private:
    bool validate();
    bool match(char a, char b) const;
    void numOfPairs(const string &s, int l, int r);
    int numOfPairsTopDown(const string &s, int l, int r);
    int numOfPairsRecursive(const string &s, int l, int r);
    void computePairs(int l, int r);
    string sequence;
    int length;
    bool valid;
    vector<vector<int>> dp;
    vector<vector<int>> jPairs;
    vector<pair<int, int>> pairs;
};

#endif // RNA_H
