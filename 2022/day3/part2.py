
def get_priority(char):
    ascii_value = ord(char)
    return ascii_value - 96 if ascii_value > 90 else ascii_value - 38


def solve(input_file):
    priority_sum = 0
    with open(input_file) as input_data:
        line = input_data.readline().strip()

        while line:
            badge = (set(line) & set(input_data.readline().strip()) & set(input_data.readline().strip())).pop()
            priority_sum += get_priority(badge)
            line = input_data.readline().strip()

    return priority_sum


if __name__ == '__main__':
    print(solve('input.txt'))
