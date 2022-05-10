formula = input().replace('\r', '')

curr_side = -1 # -1: left, 1: right
curr_symbol = 1 # -1: negative, 1: positive

start_slice = 0 # index of the start of the current number

unknown = '' # the variable in the formula
unknown_coef = 0 # the coefficient before the variable

constant = 0 # the constant (on the right side)

# unknown_coef * unknown = constant

def evaluate_number(s, mode): # mode: (co)n(stant), (co)e(fficient)
    
    global curr_side, curr_symbol

    if mode == 'n':
        if not s:
            return 0
        else:
            return curr_side * curr_symbol * int(s)
    elif mode == 'e':
        if not s:
            return -1 * curr_side * curr_symbol
        else:
            return -1 * curr_side * curr_symbol * int(s)


for i in range(len(formula)):
    
    if formula[i] in '+-=':
        
        curr_slice = formula[start_slice:i]
        
        if curr_slice:
            if curr_slice.isdigit():
                constant += evaluate_number(curr_slice, 'n')
            else:
                unknown = curr_slice[-1]
                unknown_coef += evaluate_number(curr_slice[:-1], 'e')

        if formula[i] == '+':
            curr_symbol = 1
        elif formula[i] == '-':
            curr_symbol = -1
        elif formula[i] == '=':
            curr_side = 1
            curr_symbol = 1

        start_slice = i + 1

curr_slice = formula[start_slice:]

if curr_slice.isdigit():
    constant += evaluate_number(curr_slice, 'n')
else:
    unknown = curr_slice[-1]
    unknown_coef += evaluate_number(curr_slice[:-1], 'e')

if constant == 0:
    unknown_coef = 1
print('{:}={:.3f}'.format(unknown, constant / unknown_coef))

