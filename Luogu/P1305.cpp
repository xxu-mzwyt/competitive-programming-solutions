#include <iostream>

const int MAXN = 26 * 2;

int char2int(char c);
char int2char(int i);
void print_pre(int rt);

int l_child[MAXN];
int r_child[MAXN];

int main() {
    int n;
    std::cin >> n;
    
    char root, lc, rc;
    int main_root;

    for (int i = 0; i < n; i++) {
        std::cin >> root >> lc >> rc;
        // scanf("%c%c%c", &root, &lc, &rc);
        // printf("%c %c %c\n\n\n", root, lc, rc);
        if (i == 0) main_root = char2int(root);
        l_child[char2int(root)] = char2int(lc);
        r_child[char2int(root)] = char2int(rc);
    }

    // printf("%d %d %d\n\n", main_root, l_child[main_root], r_child[main_root]);
    print_pre(main_root);

}

int char2int(char c) {
    if (c >= 'a' && c <= 'z') return c - 'a';
    else if (c >= 'A' && c <= 'Z') return c - 'A' + 26;
    else return -1;
}
char int2char(int i) {
    if (i >= 26 && i < 2 * 26) return 'A' + i - 26;
    else if (i >= 0 && i < 26) return 'a' + i;
    else return '*';
}

void print_pre(int rt) {
    if (rt == -1) return;
    //printf("%c", int2char(rt));
    std::cout << int2char(rt);
    print_pre(l_child[rt]);
    print_pre(r_child[rt]);
}
