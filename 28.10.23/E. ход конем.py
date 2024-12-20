def makeover(pos):
    makeovered_pos = [ord(pos[0]) - ord('A') + 1, int(pos[1])]
    return makeovered_pos
def unmakeover(makeovered_turn):
    return f'{chr(makeovered_turn[0]+64)}{makeovered_turn[1]}'
def list_of_turns(start_pos):
    x, y = makeover(start_pos)
    sample = [(x + 1, y + 2), (x - 1, y + 2), (x - 2, y + 1), (x - 2, y - 1), (x - 1, y - 2), (x + 1, y - 2),
              (x + 2, y + 1), (x + 2, y - 1)]
    turns = [unmakeover(el) for el in sample if ((1 <= el[0] <= 8) and (1 <= el[1] <= 8))]
    return turns
print(list_of_turns(input()))
