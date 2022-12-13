from year2022.day4.part1 import solve as part1_solve
from year2022.day4.part2 import solve as part2_solve
from year2022.utils import get_data_path


class TestPart1:
    def test_example(self):
        result = part1_solve(get_data_path(__file__, 'example.txt'))
        assert result == 2

    def test_input(self):
        result = part1_solve(get_data_path(__file__, 'input.txt'))
        assert result == 496


class TestPart2:
    def test_example(self):
        result = part2_solve(get_data_path(__file__, 'example.txt'))
        assert result == 4

    def test_input(self):
        result = part2_solve(get_data_path(__file__, 'input.txt'))
        assert result == 847
