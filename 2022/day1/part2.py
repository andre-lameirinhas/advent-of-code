
def solve(input_file):
    calories = []
    summed_calories = 0

    with open(input_file) as input_data:
        for line in input_data:
            if line != '\n':
                summed_calories += int(line)
            else:
                calories.append(summed_calories)
                summed_calories = 0
        if summed_calories:
            calories.append(summed_calories)

    return sum(sorted(calories, reverse=True)[:3])


if __name__ == '__main__':
    print(solve('input.txt'))
