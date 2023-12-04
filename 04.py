with open('04a.txt', 'rt') as f:
    cards = [len(set.intersection(*({int(n) for n in part.split()} for part in line.split(':')[1].split('|')))) for line in f]

# Part 1
print(sum(round(2 ** (card - 1)) for card in cards))

# Part 2 slow
# def card_cnt(cs, start, cnt):
#     return sum(1 + card_cnt(cs, i + 1, cs[i]) for i in range(start, start + cnt))
# print(card_cnt(cards, 0, len(cards)))

# Part 2 fast
wins = [0] * len(cards)
for i, c in reversed(list(enumerate(cards))):
    wins[i] = 1 + sum(wins[i+1:i+1+c])
print(sum(wins))
