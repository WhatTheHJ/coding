#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    
    for (int i = 1; i <= n; i++) {
        int count = 0;
        
        while(count != i) {
            printf("*"); 
            count ++;
        };
        
        printf("\n");
    }
    
    return 0;
}