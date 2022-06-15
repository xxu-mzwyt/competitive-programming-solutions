#include <cstdio>
#include <cstring>

const int MAXN = 30;

char preorder[MAXN];
char inorder[MAXN];
char postorder[MAXN];

void inpre2post(int pl, int pr, int il, int ir);

int main() {
    scanf("%s", inorder);
    scanf("%s", preorder);
    inpre2post(0, strlen(preorder), 0, strlen(inorder));
}

// A B E D F C H G
// C B A D E F G H 
// 0 1 2 3 4 5 6 7

void inpre2post(int pl, int pr, int il, int ir) {

    // printf("\npre %d %d: ", pl, pr);
    // for (int i = pl; i < pr; i++) {
    //     printf("%c", preorder[i]);
    // }
    // printf("\nin %d %d: ", il, ir);
    // for (int i = il; i < ir; i++) {
    //     printf("%c", inorder[i]);
    // }
    // printf("\n");

    if (pl == pr || il == ir) {
        return;
    }
    char root = preorder[pl];
    for (int i = il; i < ir; i++) {
        if (inorder[i] == root) {
            inpre2post(pl + 1, pl + i - il + 1, il, i); 
            inpre2post(pl + i - il + 1, pr, i + 1, ir); 
        }
    }
    printf("%c", root);

}
