
def solve(input_file):
    contains_count = 0
    with open(input_file) as input_data:
        for line in input_data:
            list_a, list_b = line.strip().split(",")
            min_a, max_a = [int(val) for val in list_a.split("-")]
            min_b, max_b = [int(val) for val in list_b.split("-")]
            if min_a >= min_b and max_a <= max_b or min_b >= min_a and max_b <= max_a:
                contains_count += 1
    return contains_count


if __name__ == '__main__':
    print(solve('input.txt'))
