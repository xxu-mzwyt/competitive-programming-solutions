#include <stack>
#include <map>
#include <cstdio>
#include <cstring>

const int MAXS = 101;

struct br {
    int pos;
    char type;
};
std::stack <br> s;

std::map <char, char> suit;
std::map <char, char> other;
std::map <char, char> paired;

char br_arr[MAXS];
char op_arr[2 * MAXS];

int main() {

    int op_ind = 0;
    suit[']'] = '[';
    suit[')'] = '('; 
    other[']'] = ')';
    other[')'] = ']';
    paired['['] = 'u';
    paired['('] = 'o';

    scanf("%s", br_arr);
    for (int i = 0; i < strlen(br_arr); i++) {
        char curr = br_arr[i];
        if (curr == '(' || curr == '[') {
            s.push((br){op_ind, curr});
            op_arr[op_ind++] = curr;
        }
        else {
            // while (!s.empty() && s.top().type != suit[curr]) {
            //     op_arr[op_ind++] = other[curr];
            //     s.pop();
            // }
            if (s.empty() || s.top().type != suit[curr]) {
                op_arr[op_ind++] = suit[curr];
            }
            else {
                s.pop();
            }
            op_arr[op_ind++] = curr;
        }
    }
    
    while (!s.empty()) {
        op_arr[s.top().pos] = paired[s.top().type];
        s.pop();
    }

    for (int i = 0; i < op_ind; i++) {
        if (op_arr[i] == 'u') {
            printf("[]");
        }
        else if (op_arr[i] == 'o') {
            printf("()");
        }
        else {
            printf("%c", op_arr[i]);
        }
    }

}

// int main() 
//     scanf("%s", br_arr);
//     for (int i = 0; i < strlen(br_arr); i++) {
//         char curr = br_arr[i];
//         if (curr != '(' && curr != ')' && curr != '[' && curr != ']') {
//             break;
//         }
//         if (curr == '(' || curr == '[') {
//             s.push(curr);
//         } 
//         else {
//             if (curr == ')') {
//                 while (!s.empty() && s.top() == '[') {
//                     s.pop();
//                     printf("]");
//                 }
//                 if (s.empty()) {
//                     printf("(");
//                 }
//                 else {
//                     s.pop();
//                 }
//             }
//             else {
//                 while (!s.empty() && s.top() == '(') {
//                     s.pop();
//                     printf(")");
//                 }
//                 if (s.empty()) {
//                     printf("[");
//                 }
//                 else {
//                     s.pop();
//                 }
//             }
//         }
//         printf("%c", curr);
//     }
//     while (!s.empty()) {
//         if (s.top() == '(') {
//             printf(")");
//         }
//         else {
//             printf("]");
//         }
//         s.pop();
//     }
// }
