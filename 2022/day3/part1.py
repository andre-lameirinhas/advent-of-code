
def get_priority(char):
    ascii_value = ord(char)
    return ascii_value - 96 if ascii_value > 90 else ascii_value - 38


def solve(input_file):
    priority_sum = 0
    with open(input_file) as input_data:
        for line in input_data:
            line = line.strip()
            midpoint = len(line) // 2
            item_type = (set(line[:midpoint]) & set(line[midpoint:])).pop()
            priority_sum += get_priority(item_type)
    return priority_sum


if __name__ == '__main__':
    print(solve('input.txt'))
