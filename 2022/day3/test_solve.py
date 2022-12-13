from day3.part1 import solve as part1_solve
from day3.part2 import solve as part2_solve
from utils import get_data_path


class TestPart1:
    def test_example(self):
        result = part1_solve(get_data_path(__file__, 'example.txt'))
        assert result == 157

    def test_input(self):
        result = part1_solve(get_data_path(__file__, 'input.txt'))
        assert result == 7746


class TestPart2:
    def test_example(self):
        result = part2_solve(get_data_path(__file__, 'example.txt'))
        assert result == 70

    def test_input(self):
        result = part2_solve(get_data_path(__file__, 'input.txt'))
        assert result == 2604
