inorder = input().strip()
postorder = input().strip()

def preorder(ino, posto):
    if len(ino) <= 1:
        print(ino, end='')
    else:
        root = posto[-1]
        print(root, end='')
        l_ino = ino[:ino.find(root)]
        r_ino = ino[ino.find(root) + 1:]
        l_posto = posto[:len(l_ino)]
        r_posto = posto[len(l_ino):-1]
        preorder(l_ino, l_posto)
        preorder(r_ino, r_posto)

preorder(inorder, postorder)    
