def shuffle(deck, k):

    new_deck = []
    
    for i in range(k // 2):
        new_deck.append(deck[k // 2 + i])
        new_deck.append(deck[i])
    
    return new_deck    

deck = []
n, k, m, p = map(int, input().strip().split())
for i in range(k):
    deck.append(input().strip())
deck = tuple(deck)
for i in range(m):
    deck = shuffle(deck, k)
    if k % 2:
        k -= 1
if k <= 4 * n:
    print("Error:cards not enough")
else:
    for i in range(4):
        print(deck[i * n + p - 1])

