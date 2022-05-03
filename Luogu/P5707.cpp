#include <stdio.h>
#include <math.h>

int const HOUR_TO_MINUTE = 60;
int const DEADLINE = 8;
int const DAY_TO_HOUR = 24; 

int main() {
	int s, v;
	scanf("%d%d", &s, &v);
	int time_minutes = ceil((double) s / v) + 10;
	int start_hours, start_minutes;
	if (time_minutes > HOUR_TO_MINUTE * DEADLINE) {
		time_minutes -= HOUR_TO_MINUTE * DEADLINE;
		start_hours = DAY_TO_HOUR - ceil((double) time_minutes / HOUR_TO_MINUTE);
		start_minutes = HOUR_TO_MINUTE - time_minutes % HOUR_TO_MINUTE;
		if (start_minutes == 60) {
			start_minutes = 0;
		}
		
	}
	else {
		start_hours = DEADLINE - ceil((double) time_minutes / HOUR_TO_MINUTE);
		start_minutes = HOUR_TO_MINUTE - time_minutes % HOUR_TO_MINUTE;
		if (start_minutes == 60) {
			start_minutes = 0;
		}
	}
		
	// printf("%d\n", time_minutes);	
	printf("%02d:%02d", start_hours, start_minutes);
	
	return 0;
}
