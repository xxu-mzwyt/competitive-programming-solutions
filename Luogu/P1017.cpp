#include <stdio.h>

const int MAXD = 20;

int output[MAXD];
int output_cnt = 0;


void dec2r(int num, int R, int rslt[]);
void print_rslt(int rslt[]);


int main() {

	int n, r;
	scanf("%d%d", &n, &r);
	printf("%d=", n);
	
	dec2r(n, r, output);
	
	print_rslt(output);
	
	printf("(base%d)", r);
	
	return 0;
	
}


void dec2r(int num, int R, int rslt[]) {
	
	int dgt;
	while(num != 0) {
		dgt = num % R;
		if (dgt < 0) {
			dgt -= R;
		}
		rslt[output_cnt] = dgt;
		output_cnt++;
		num = (num - dgt) / R;
	}	
	
}

void print_rslt(int rslt[]) {
	
	for (int i = output_cnt - 1; i >= 0; i--) {
		if (rslt[i] < 10) printf("%d", rslt[i]);
		else printf("%c", rslt[i] - 10 + 'A');
	}
	
}
