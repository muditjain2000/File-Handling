#include<stdio.h>


int main() {

FILE *filePointer ;
filePointer = fopen("sample.txt", "w+"); fprintf(filePointer, "%s %s %d %s", "I", "had", 3,"toys");



char str1[20] = "";

char str2[20] = "";

char str3[20] = ""; int count; rewind(filePointer);
fscanf(filePointer, "%s %s %d %s", str1, str2, &count,str3);



printf("%s %s %d %s \n", str1, str2, count, str3); fclose(filePointer);
}
