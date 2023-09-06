/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
/*#include <iostream>

using namespace std;

int main()
{
int n=6,i,j;
for(i=1;i<n;i++){
    for(j=1;j<2*(n-i);j++){
        cout << " ";
    }
    for(j=i;j>=1;j--){
        cout << j << " ";
    }
    for(j=2;j<=i;j++){
        cout << j << " ";
    }
    cout << "\n";
}
}*/
/*#include <iostream>

using namespace std;

int main()
{
int n=4,i,j,num=1;
for(i=1;i<=n;i++){
    for(j=1;j<=i;j++){
        cout << num ;
        num++;
    }
    cout << "\n";
}
}*/
/*#include <iostream>

using namespace std;

int main()
{
int n=5,i,j,num=2;
for(i=1;i<=n;i++){
    for(j=1;j<=i;j++){
        if(i%n!=0){
            num++;
        }
        cout << num ;
    }
    cout << "\n";
}
}*/
/*#include <iostream>

using namespace std;

int main()
{
int n=6,i,j;
for(i=1;i<n;i++){
    for(j=1;j<2*(n-i);j++){
        cout << " ";
    }
    for(j=i;j>=1;j--){
        cout << " *";
    }
    for(j=2;j<=i;j++){
        cout << " *";
    }
    cout << "\n";
}
for(i=4;i>=1;i--){
    for(j=1;j<2*(n-i);j++){
        cout << " ";
    }
    for(j=i;j>=1;j--){
        cout << " *";
    }
    for(j=2;j<=i;j++){
        cout << " *";
    }
    cout << "\n";
}
}*/
/*#include <iostream>

using namespace std;

int main()
{
int n=6,i,j;
for(i=4;i>1;i--){
    for(j=1;j<2*(n-i);j++){
        cout << " ";
    }
    for(j=i;j>=1;j--){
        cout << " *";
    }
    for(j=2;j<=i;j++){
        cout << " *";
    }
    cout << "\n";
}
for(i=1;i<n;i++){
    for(j=1;j<2*(n-i);j++){
        cout << " ";
    }
    for(j=i;j>=1;j--){
        cout << " *";
    }
    for(j=2;j<=i;j++){
        cout << " *";
    }
    cout << "\n";
}

}*/
/*#include <iostream>

using namespace std;

int main()
{
int n=5,i,j;
for(i=1;i<=n;i++){
    for(j=1;j<=i;j++){
        cout << " *";
    }
    cout << "\n";
}
for(i=4;i>=1;i--){
    for(j=1;j<=i;j++){
        cout << " *";
    }
    cout << "\n";
}
}*/
/*#include <iostream>

using namespace std;

int main()
{
int n=6,i,j;
for(i=1;i<n;i++){
    for(j=1;j<2*(n-i);j++){
        cout << " ";
    }
   for(j=i;j>=1;j--){
        cout << "* ";
    }
    cout << "\n";
}
for(i=4;i>=1;i--){
    for(j=1;j<2*(n-i);j++){
        cout << " ";
    }
   for(j=i;j>=1;j--){
        cout << "* ";
    }
    cout << "\n";
}
}*/
#include <iostream>

using namespace std;

int main()
{
int n=6,i,j;
for(i=1;i<n;i++){
   for(j=i;j>=1;j--){
        cout << "* ";
    }
    cout << "\n";
}
}
/*#include <iostream>

using namespace std;

int main()
{
   int i,j,n=5;
   for(i=0;i<n;i++){
       for(j=n;j>=i;j--){
           cout << " ";
       }
       for(j=1;j<=i;j++){
           cout << i << " ";
       }
       cout << "\n";
   }
      for(i=3;i>=1;i--){
       for(j=n;j>=i;j--){
           cout << " ";
       }
       for(j=1;j<=i;j++){
           cout << i << " ";
       }
       cout << "\n";
   }

}*/
/*#include <iostream>

using namespace std;

int main()
{
   int i,j,n=5;
   for(i=n;i>=1;i--){
       for(j=n;j>=i;j--){
           cout << "  ";
       }
       for(j=1;j<=2*i-1;j++){
           cout << i << " ";
       }
       cout << "\n";
   }
      for(i=2;i<=n;i++){
       for(j=n;j>=i;j--){
           cout << "  ";
       }
       for(j=1;j<=2*i-1;j++){
           cout << i << " ";
       }
       cout << "\n";
   }

}*/

/*#include <iostream>

using namespace std;

int main()
{
   char i,j;
   for(i=65;i<=70;i++){
       for(j=65;j<=i;j++){
           cout << i<<" ";
       }
       cout<<"\n";
   }
}*/
#include <iostream>

using namespace std;

int main()
{
   char i,j;
   for(i=65;i<=69;i++){
       for(j=65;j<=i;j++){
           cout << " ";
       }
      for(j=69;j>=65;j--){
           cout << i<<" ";
       }
       cout<<"\n";
   }
}
# List - ordered,mutable,duplicate allowed []
# Tuple - ordered,immutable,duplicate allowed ()

t1= (1,2,3.4,'hi',True)
print(t1)
print(t1[0])
print(t1[0:3])
print(t1[3:])
print(t1[:4])
print(t1[-2])
print(t1[-3:-1])
