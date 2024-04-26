#include "rnaProfile.h"

ProfileRNA::ProfileRNA(string s)
{
    sequence = s;
    length = s.length();
    valid = validate();

    if (valid)
    {
        dp = vector<vector<int>>(length, vector<int>(length, -1));
        jPairs = vector<vector<int>>(length, vector<int>(length, -1));
        numOfPairs(sequence, 0, length - 1);
        computePairs(0, length - 1);
        if (pairs.size() != dp[0][length - 1])
            cout << "Wut" << endl;

        sort(pairs.begin(), pairs.end());
    }
    else
        cout << "Invalid RNA sequence" << endl;
}

void ProfileRNA::printPairs() const
{
    if (!valid)
        return;
    ofstream outfile("out.txt");
    if (outfile.is_open())
    {
        for (auto p : pairs)
            outfile << "{" << p.first << ", " << p.second << "} ";
        outfile.close();
    }
}

bool ProfileRNA::validate()
{
    for (char c : sequence)
        if (c != 'A' && c != 'U' && c != 'G' && c != 'C')
            return false;
    return true;
}

bool ProfileRNA::match(char a, char b) const
{
    if ((a == 'A' && b == 'U') || (a == 'U' && b == 'A') ||
        (a == 'G' && b == 'C') || (a == 'C' && b == 'G'))
        return true;
    return false;
}

void ProfileRNA::numOfPairs(const string &s, int l, int r)
{
    for (int i = 0; i < length; i++)
    {
        for (int j = 0; j < length; j++)
        {
            if (i >= j - 4)
                dp[i][j] = 0;
        }
    }

    for (int k = 5; k < s.length(); k++)
    {
        for (int i = 0; i + k < s.length(); i++)
        {
            int j = i + k;
            dp[i][j] = max(dp[i][j], dp[i][j - 1]);

            for (int t = i; t <= j - 5; t++)
            {
                if (match(s[t], s[j]))
                {
                    int temp =
                        1 + (t >= 1 ? dp[i][t - 1] : 0) + dp[t + 1][j - 1];
                    if (dp[i][j] < temp)
                    {
                        dp[i][j] = temp;
                        jPairs[i][j] = t;
                    }
                }
            }
        }
    }
}

void ProfileRNA::computePairs(int l, int r)
{
    if (l > r || l < 0 || r < 0)
        return;
    if (jPairs[l][r] == -1)
        return computePairs(l, r - 1);
    pairs.push_back({jPairs[l][r], r});
    computePairs(l, jPairs[l][r] - 1);
    computePairs(jPairs[l][r] + 1, r - 1);
}

int main(int argc, char **argv)
{
    string s;
    ifstream infile(argv[1]);
    if (infile.is_open())
    {
        getline(infile, s);
        infile.close();
    }
    ProfileRNA obj(s);
    obj.printPairs();
}
