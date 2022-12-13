
def move_score(opponent, player):
    return {
        ('A', 'X'): 3, ('A', 'Y'): 1, ('A', 'Z'): 2,
        ('B', 'X'): 1, ('B', 'Y'): 2, ('B', 'Z'): 3,
        ('C', 'X'): 2, ('C', 'Y'): 3, ('C', 'Z'): 1,
    }[(opponent, player)]


def outcome_score(outcome):
    return {'X': 0, 'Y': 3, 'Z': 6}[outcome]


def solve(input_file):
    final_score = 0
    with open(input_file) as input_data:
        for line in input_data:
            opponent, player = [move.strip() for move in line.split(' ')]
            final_score += move_score(opponent, player) + outcome_score(player)
    return final_score  # 10349


if __name__ == '__main__':
    print(solve('input.txt'))
