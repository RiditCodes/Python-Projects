#include<iostream>
using namespace std;

int main(){
    int num, binary = 0, remainder = 0, product = 1;
    cout<<"Enter a number to convert into binary: ";
    cin>>num;
    while(num != 0){
        remainder = num % 2;
        binary = binary + (remainder * product);
        num /= 2;
        product *= 10;
    }
    cout<<"The binary form is: "<<binary;
}