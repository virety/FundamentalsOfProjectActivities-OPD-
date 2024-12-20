def fill(depth, i):
    left = tree[2 * i]
    tour_num = n - depth
    for pl in players_won.get(left):
        if wins_of_player.get(pl, 0) == tour_num:
            sus = pl
            break
    return sus
with open('input.txt', encoding="utf-8") as file:
    s = [i.strip().split("  ") for i in file.readlines()]
    n = int(s[0][0])
    del s[0]
    q = []
    for i in s:
        for j in i:
            q.append(j)

    tree = ["."] + [-1] * (2 ** (n + 1) - 1)
    matches = []

    for i in range(2 ** n - 1):
        matches.append(list(map(int, q[i].split())))

    players = [[0] * (n + 1) for _ in range(n + 1)]
    wins = [0] * (n + 1)

    for i in matches:
        winner, loser = i[0], i[1]
        players[winner][wins[winner]] = loser
        wins[winner] += 1

    abs_winner = max(range(1, n + 1), key=lambda x: wins[x])
    tree[1] = abs_winner

    max_depth = (2 ** (n + 1)) // 2 - 1
    for i in range(1, max_depth + 1):
        if tree[i] != -1:
            if tree[2 * i] == -1:
                tree[2 * i] = tree[i]
            else:
                k = i
                while tree[k] != -1:
                    k = 2 * k
                k = k // 2
                tree[2 * i + 1] = fill(k, i)

with open('output.txt', 'w') as f:
    res = tree[2**n:]
    f.write(" ".join(map(str, res)))
