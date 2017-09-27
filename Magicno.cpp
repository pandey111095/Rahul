#include<bits/stdc++.h>
using namespace std;
int main()
 {
	//code
        int  t;
        cin>>t;
        while(t--)
       {
           int n;
           cin>>n;
           int a[n],to=1;
           a[0]=5;
          for(int i=2;to<=n;i++)
           {
               a[to++]=pow(5,i);
               int te=to;
               for(int j=0;j<te-1;j++)
               {
                   if(to<n)
                   a[to++]=a[j]+a[te-1];
                   else
                   break;
               }
           }
           cout<<a[n-1]<<endl;
       }
       return 0;
}
