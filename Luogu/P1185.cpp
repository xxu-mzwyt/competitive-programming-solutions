#include <iostream>
#include <string>

const int MAXM = 10 + 1;
const int MAX_POW2 = 1024; 

int stick_len[MAXM], pow_2[MAXM];
int to_remove[MAXM][MAX_POW2];
// 0: keep both
// 1: keep left
// 2: keep right
// 3: remove both 
// 4: removed node (and all its children)

int remove_left[5] = {2, 3, 2, 3, 4};
int remove_right[5] = {1, 1, 3, 3, 4};

// TO FIX
// node w/ no child != no node

void init();
void draw_leaf(int curr_lyr, int max_lyr);
void draw_stick(int curr_lyr, int max_lyr);
void remove_node(int lyr, int num, int max_lyr);

std::string operator * (std::string c, unsigned int n) {
    std::string output = "";
    while (n--) {
        output += c;
    }
    return output;
}


int main() {
    int m, n;
    std::cin >> m >> n;
    init();
    for (int i = 0; i < n; i++) {
        int lyr, num;
        std::cin >> lyr >> num;
        lyr--, num--;
        remove_node(lyr, num, m);
        if (num < pow_2[lyr]) {
            if (lyr > 0 && num % 2 == 0) {
                to_remove[lyr - 1][num / 2] = remove_left[to_remove[lyr - 1][num / 2]];
            }
            if (lyr > 0 && num % 2 == 1) {
                to_remove[lyr - 1][num / 2] = remove_right[to_remove[lyr - 1][num / 2]];
            }
        }
    }
    for (int i = 0; i < m; i++) {
        draw_leaf(i, m);
        draw_stick(i, m);
    }
}


void init() {
    stick_len[0] = 0, stick_len[1] = 1;
    pow_2[0] = 1, pow_2[1] = 2;
    int sum = 1;
    for (int i = 2; i < MAXM; i++) {
        stick_len[i] = sum + i - 1;
        sum += stick_len[i];
        pow_2[i] = pow_2[i - 1] * 2;
    }
    // for (int i = 0; i < MAXM; i++) {
    //     std::cout << pow_2[i] << ' ';
    // }

    // 0 1 2 5 11 23 47 95 191 383
}

void draw_leaf(int curr_lyr, int max_lyr) {
    int curr_gap = stick_len[max_lyr - curr_lyr];
    if (curr_gap == 1) {
        curr_gap = 0;
    }
    for (int i = 0; i < pow_2[curr_lyr]; i++) {
        std::cout << (std::string)" " * curr_gap;
        if (to_remove[curr_lyr][i] == 4) {
            std::cout << " ";
        }
        else {
            std::cout << "o";
        }
        std::cout << (std::string)" " * curr_gap;
        if (curr_gap == 0 && i % 2 == 0) {
            std::cout << "   ";
        }
        else {
            std::cout << " ";
        }
    }
    std::cout << "\n";
}

void draw_stick(int curr_lyr, int max_lyr) {
    int curr_len = stick_len[max_lyr - curr_lyr - 1];
    int curr_gap = stick_len[max_lyr - curr_lyr] - curr_len;
    for (int i = 0; i < curr_len; i++) {
        for (int j = 0; j < pow_2[curr_lyr]; j++) {
            std::cout << (std::string)" " * (curr_gap + curr_len - i - 1);
            if (to_remove[curr_lyr][j] == 2 || to_remove[curr_lyr][j] >= 3) {
                std::cout << " ";
            }
            else {
                std::cout << "/";
            }
            std::cout << (std::string)" " * (2 * i + 1);
            if (to_remove[curr_lyr][j] == 1 || to_remove[curr_lyr][j] >= 3) {
                std::cout << " ";
            }
            else {
                std::cout << "\\";
            }
            std::cout << (std::string)" " * (curr_gap + curr_len - i);
        }
        std::cout << "\n";
    }
}

void remove_node(int lyr, int num, int max_lyr) {
    if (lyr >= max_lyr) {
        return;
    }
    to_remove[lyr][num] = 4;
    remove_node(lyr + 1, num * 2, max_lyr);
    remove_node(lyr + 1, num * 2 + 1, max_lyr);
}
