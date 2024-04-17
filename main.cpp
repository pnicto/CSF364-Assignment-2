#include "include/rna.h"

int main()
{
    string s;
    cout << "Enter RNA sequence: " << endl;
    getline(cin, s);

    RNA r(s);
    r.printPairs();
    return 0;
}