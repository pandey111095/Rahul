#include <iostream>
#include<cmath>
using namespace std;

int main() {
	//code
	int i,j,t,n,c=0,k;
	cin>>t;
	for(i=0;i<t;i++)
	{
	    cin>>n;
	    int a[n],tot=0;
	    for(j=0;j<n;j++)
	    {
	        cin>>a[j];
	        if(j==n-1)
	        {
	            c=0;
	            a[j]+=1;
	            if(a[j]==10)
	            {
	                a[j]=0;
	                c=1;
	            
	            }
	        }
	    }
	    if(c==1)
	    {
	        for(j=n-2;j>=0;j--)
	        {
	            if(c!=1)
	                break;
	            c=0;
	             
	            a[j]+=1;
	            if(a[j]==10)
	            {
	                
	                a[j]=0;
	                c=1;
	            }
	        }
	        if(c==1)
	        {
	            cout<<"1"<<" ";
	            for(k=0;k<n;k++)
	               cout<<"0"<<" "; 
	        }
	        else
	        {
	            for(k=0;k<n;k++)
	               cout<<a[k]<<" "; 
	        }
	    }
	    else
	    {
        for(j=0;j<n;j++)
           cout<<a[j]<<" "; 
	    }
	    cout<<endl;
	}
	return 0;
}

