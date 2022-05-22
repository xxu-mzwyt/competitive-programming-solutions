totem = " /\\ \n/__\\"

n = int(input().strip())

def indent(s, l):
    rslt = ""
    for i in s.split("\n"):
        rslt += " " * l + i + " " * l + "\n"
    return rslt

for i in range(1, n):
    new_totem = indent(totem, 2 ** i)
    for i in totem.split("\n"):
        new_totem += i * 2 + "\n"
    totem = new_totem[:-1]

print(totem)

