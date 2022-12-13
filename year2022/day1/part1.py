
def solve(input_file):
    max_calories = 0
    local_max_calories = 0

    with open(input_file) as input_data:
        for line in input_data:
            if line != '\n':
                local_max_calories += int(line)
            else:
                if local_max_calories > max_calories:
                    max_calories = local_max_calories
                local_max_calories = 0
        if local_max_calories > max_calories:
            max_calories = local_max_calories

    return max_calories


if __name__ == '__main__':
    print(solve('input.txt'))
