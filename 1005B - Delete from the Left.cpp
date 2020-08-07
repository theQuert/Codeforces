#include <iostream>
#include <cstdlib>
#include <string>
#include <cmath>

using namespace std;

int main()
{
    string s, t;
    cin >> s >> t;

    long moves(0);
    bool diff(false);
    for(long p = s.size() - 1, q = t.size() - 1; p >= 0 || q >= 0; p--, q--)
    {
        if(p < 0 || q < 0) {++moves; continue;}
        if(s[p] != t[q]) {diff = true;}
        if(diff) {moves += 2;}
    }

    cout << moves << endl;
        
    return 0;
}
