#include <stdio.h>

int main(){
	int a = 0;
	int b = 0;
	int i;
	int j;
	for (i = 0; i < 20 ; i++){
		a = a + 1;
		for (j = 0; j < 15 ; j++){
			b = b + 1;
		}
	}
	printf("a is %d\n", a);
	printf("b is %d\n", b); 
}
