#include <iostream>
#include <math.h>

using namespace std;

int c = 1;

bool Comprobar(int Queens[], int n, int k){
    for(int i = 0; i < k; i++)
        if((Queens[k] == Queens[i]) || (abs(k-i) == abs(Queens[k] - Queens[i])))
            return false;
    return true;
}

void NQueens(int Queens[], int n, int k){
    if(n==k){
        cout << "Solucion "<<c<<": ";
        for(int i = 0; i<n; i++)
            cout << Queens[i] << ' ';
        cout << endl;
        c++;
        return;
    }

    for(int i = 0; i < n; i++){
        Queens[k] = i;
        if(Comprobar(Queens, n, k))
            NQueens(Queens, n, k+1); 
    }

}

int main(){
    int N = 12;
    int *Queens = new int(N);
    NQueens(Queens, N, 0);
}