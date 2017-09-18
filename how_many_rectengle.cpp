#include<bits/stdc++.h>
using namespace std;
int main()
{
    int  t;
    cin>>t;
    while(t--)
    {
        int n,m,c=0;
        cin>>n>>m;
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=m;j++)
            {
                c+=(n-i+1)*(m-j+1);
            }
        }
        cout<<c<<endl;
    }
    return 0;
}
