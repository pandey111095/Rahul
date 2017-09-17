#include<bits/stdc++.h>
using namespace std;
int main()
 {
	//code
        int  t;
        cin>>t;
        while(t--)
       {
           int i,j;
           string str1,str2;
           cin>>str1>>str2;
           for(i=0;i<str1.length();i++)
           {
               for(j=0;j<str2.length();j++)
               {
                   if(str1[i]==str2[j])
                   {
                       str2[j]=' ';
                       break;
                   }
               }
               if(j==str2.length())
                break;
           }
           if(i==str1.length())
            cout<<"YES"<<endl;
            else
            cout<<"NO"<<endl;
       }
       return 0;
}
