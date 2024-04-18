#include "include/rna.h"

int main()
{
    string s, d_s;

    ifstream infile("in.txt");
    if (infile.is_open())
    {
        getline(infile, s);
        infile.close();
    }

    ifstream d_infile("d_in.txt");
    if (d_infile.is_open())
    {
        getline(d_infile, d_s);
        d_infile.close();
    }

    RNA r(s, d_s);
    r.printPairs();
    return 0;
}