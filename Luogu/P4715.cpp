#include <cstdio>

int n;
int team_cnt = 1;

struct Team {
    int atk;
    int cnt;
};

Team play_game(int dep) {
    
    Team a, b;
    if (dep == n - 1) {
        scanf("%d%d", &a.atk, &b.atk);
        a.cnt = team_cnt++;
        b.cnt = team_cnt++;
    }
    else {
        a = play_game(dep + 1);
        b = play_game(dep + 1);
    }
    
    if (dep == 0) {
        return a.atk > b.atk ? b : a;
    }
    else {
        return a.atk > b.atk ? a : b;
    }

}


int main() {
    
    scanf("%d", &n);
    printf("%d", play_game(0).cnt); 

}
