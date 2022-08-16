#include<stdio.h>
#include<stdlib.h>

int main(){
    int* ptr;
    int n, i;
    scanf("%d", &n);
    ptr = (int*)malloc(n * sizeof(int));
    if(ptr == NULL){
        printf("memory is not allocated");
        exit(0);
    } else {
        printf("memory has been allocated");
        printf("add numbers in the pointer");

        for(int i=0; i<n; i++){
            scanf("%d", ptr+i);
        }
        for(int i=0; i<n; i++){
            printf("%d", ptr[i]);
        }

    }
    free(ptr);
    return 0;
}