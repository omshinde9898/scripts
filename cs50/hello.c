#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int print_arr(int n[]);

int main(void){
    int a[10] = {10,20,30,40,60,50,70,80,90,0};
    print_arr(a);
    char name[20];
    printf("Enter Name : ");
    scanf("%s",name);
    printf("Hello, %s",name);
    return 0;
}

int print_arr(int n[]){
    for(int i; i<10;i++){
        printf("%i \n",n[i]);
    }
    return 0;
}

struct node
{
    int number;
    struct node* next;
};
node;


