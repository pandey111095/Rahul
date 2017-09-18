#include<bits/stdc++.h>
using namespace std;
int main()
{
    int  t;
    cin>>t;
    while(t--)
    {
        int n,m;
        cin>>m>>n;
        string s;
        for(int i=1;i<=n;i++)
        {
            long p=pow(m,i);
            string s=to_string(p);
            cout<<s[0];
            cout<<p%10;
        }
        cout<<endl;
    }
    return 0;
}
