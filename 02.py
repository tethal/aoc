from collections import defaultdict


def parse(line):
    rgb = lambda s: defaultdict(int, {x.split()[1]: int(x.split()[0]) for x in s.split(', ')})
    return int(line.split(':')[0].removeprefix("Game ")), tuple(map(rgb, line.split(':')[1].strip().split('; ')))


with open('02a.txt', 'rt') as f:
    # part1: print(sum(line[0] for line in map(parse, f) if all(game['red'] <= 12 and game['green'] <= 13 and game['blue'] <= 14 for game in line[1])))
    print(sum(max(v['red'] for v in game[1]) * max(v['green'] for v in game[1]) * max(v['blue'] for v in game[1]) for game in map(parse, f)))
