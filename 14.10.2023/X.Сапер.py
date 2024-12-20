def build_field(N, M, K, mines):
    field = [[0] * M for k in range(N)]
    for mine in mines:
        row, col = mine
        field[row - 1][col - 1] = '*' 
        for i in range(max(0, row-2), min(N, row+1)):
            for j in range(max(0, col-2), min(M, col+1)):
                if field[i][j] != '*':
                    field[i][j] += 1
    return field
N, M, K = map(int, input().split())
mines = [list(map(int, input().split())) for i in range(K)]
field = build_field(N, M, K, mines)
for row in field:
    print(' '.join(map(str, row)))
