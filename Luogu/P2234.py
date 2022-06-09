from random import random

sales_log = None
# l r val pri
# 0 1 2   3

def lrot(t):
    if not t or not t[1]:
        return t
    else:
        temp = t[1]
        t[1] = temp[0]
        temp[0] = t
        return temp

def rrot(t):
    if not t or not t[0]:
        return t
    else:
        temp = t[0]
        t[0] = temp[1]
        temp[1] = t
        return temp

def insert(t, v):
    if not t:
        return [None, None, v, random()]
    else:
        if t[2] < v:
            t[1] = insert(t[1], v)
            if t[1][3] < t[3]:
                t = lrot(t)
        elif t[2] > v:
            t[0] = insert(t[0], v)
            if t[0][3] < t[3]:
                t = rrot(t)
        return t

def find_nearest(t, v):

    def pre(t, v):
        if not t:
            return float("-inf")
        elif t[2] > v:
            return pre(t[0], v)
        else:
            return max(t[2], pre(t[1], v))
    def bac(t, v):
        if not t:
            return float("+inf")
        elif t[2] < v:
            return bac(t[1], v)
        else:
            return min(t[2], bac(t[0], v))
    
    return min(v - pre(t, v), bac(t, v) - v)


n = int(input().strip())

sales_log = None
rslt = 0
for i in range(n):
    ai = int(input().strip())
    if not sales_log:
        rslt += ai
    else:
        rslt += find_nearest(sales_log, ai)
    sales_log = insert(sales_log, ai) 
    
print(rslt)
    



# test = [[[None, None, 3, 0], [None, None, 4, 0], 2, 0], [None, None, 5, 0], 1, 0]
# print(insert(test, 9))

# from random import random
# 
# MAXN = 32767
# 
# l = [None] * MAXN
# r = [None] * MAXN
# val = [None] * MAXN
# pri = [None] * MAXN
# 
# 
# def lrot(tr)
#     temp = r[tr]
#     r[tr] = l[temp]
#     l[temp] = tr
#     return temp
# 
# def rrot(tr):
#     temp = l[tr]
#     l[tr] = r[temp]
#     r[temp] = tr
#     return temp
# 
# def insert(tr, v):
#     if val[tr] == None:
#         val[tr] = v
#         pri[tr] = random()
# 




# def lro(log):
#     if log == None:
#         return None
#     else:
#         temp = log[1]
#         log[1] = temp
# 
# def insert(log, v):
#     if log == None:
#         return [None, v, None]
#     elif v > log[1]:
#         return [log[0], log[1], insert(log[2], v)]
#     elif v < log[1]:
#         return [insert(log[0], v), log[1], log[2]]
#     else:
#         return log
# 
# def find_nearest(log, v):
# 
#     def pre(log, v):
#         if log == None:
#             return float("-inf")
#         elif log[1] > v:
#             return pre(log[0], v)
#         else:
#             return max(log[1], pre(log[2], v))
#     def bac(log, v):
#         if log == None:
#             return float("+inf")
#         elif log[1] < v:
#             return bac(log[2], v)
#         else:
#             return min(log[1], bac(log[0], v))
#     
#     return min(v - pre(log, v), bac(log, v) - v)
# 
# 
# n = int(input().strip())
# 
# sales_log = None
# rslt = 0
# for i in range(n):
#     ai = int(input().strip())
#     if sales_log == None:
#         rslt += ai
#     else:
#         rslt += find_nearest(sales_log, ai)
#     sales_log = insert(sales_log, ai) 
#     
# print(rslt)
# 
