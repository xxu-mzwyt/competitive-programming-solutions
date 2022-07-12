ORD_DIFF = 96

def find(tr, wd):
    
    if not wd:
        return tr[0]
    elif tr[wd[0]] == None:
        return False
    else:
        return find(tr[wd[0]], wd[1:])
    

def insert(tr, wd):
    
    if not wd:
        tr[0] = True
        return tr
    
    if tr[wd[0]] == None:
        tr[wd[0]] = [False] + [None] * 26

    return 

        

# def find(tr, wd):
#    
#     if type(tr) is not dict:
#         return False 
#     elif wd[0] not in tr.keys():
#         return False
#     elif len(wd) == 1:
#         if tr[wd] == 0:
#             return False
#         else:
#             return True
#     else:
#         return find(tr[wd[0]], wd[1:])
#         
# def insert(tr, wd):
# 
#     if type(tr) is not dict:
#         return insert
# 
#     if wd[0] in tr.keys():
#         insert



t = int(input().strip())

for _ in range(t):

    n = int(input().strip())

    s_trie = {}
    
    for _ in range(n):
        s = input().strip()
        for l in s:
            if 
