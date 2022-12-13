
def move_score(move):
    return {'X': 1, 'Y': 2, 'Z': 3}[move]


def outcome_score(opponent, player):
    return {
        ('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
        ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
        ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3,
    }[(opponent, player)]


def solve(input_file):
    final_score = 0
    with open(input_file) as input_data:
        for line in input_data:
            opponent, player = [move.strip() for move in line.split(' ')]
            final_score += move_score(player) + outcome_score(opponent, player)
    return final_score  # 11063


if __name__ == '__main__':
    print(solve('input.txt'))
