#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include  <string.h>

char* solution(const char* my_string) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.

    char* answer = (char*)malloc(sizeof(char) * (strlen(my_string))+1);
    int count = 0;

    for (int i = 0; i < strlen(my_string); i++){
        if(!(my_string[i] == 'a' || my_string[i] == 'e' || my_string[i] == 'i' || my_string[i] == 'o' || my_string[i] == 'u')){
            answer[count] = my_string[i];
            count++;
        }
    }
    answer[count] = '\0';
    return answer;
}