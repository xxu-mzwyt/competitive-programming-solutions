#include <string.h>
#include <stdio.h>

const int MAXD = 150; // 100 digits max & 30 steps max 

char M[MAXD];
int num[MAXD];
int rev[MAXD];
	
int char2dec(char c);
void reverse(int n[], int r[], int len);
bool compare(int n[], int r[], int len);
int lstadd(int n[], int r[], int N, int len);

int main(){

	int N;
	scanf("%d", &N);
	scanf("%s", M);
	
	int lstlen = strlen(M);
	for (int i = lstlen - 1, j = 0; i >= 0; i--, j++) {
		num[j] = char2dec(M[i]);
	}
	
	int step = 0;
	while (step <= 30) {
		reverse(num, rev, lstlen);
		if (compare(num, rev, lstlen)) {
			printf("STEP=%d", step);
			break;
		} 
		lstlen = lstadd(num, rev, N, lstlen);
		step++;
	}
	if (step > 30) {
		printf("Impossible!");
	}
}

int char2dec(char c) {
	if (c >= '0' && c <= '9') return c - '0';
	else if (c >= 'a' && c <= 'f') return c - 'a' + 10;
	else if (c >= 'A' && c <= 'F') return c - 'A' + 10;
}

void reverse(int n[], int r[], int len) {
	for (int i = 0, j = len - 1; i < len; i++, j--) {
		r[j] = n[i];
	}
}

bool compare(int n[], int r[], int len) {
	for (int i = 0; i < len; i++) {
		if (n[i] != r[i]) {
			return false;
		}
	}
	return true;
}

int lstadd(int n[], int r[], int N, int len) {
	for(int i = 0; i < len; i++) {
		n[i + 1] += (n[i] + r[i]) / N;
		n[i] = (n[i] + r[i]) % N;
	}
	if (n[len]) return len + 1;
	else return len;
}
