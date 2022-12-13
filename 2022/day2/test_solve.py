from day2.part1 import solve as part1_solve
from day2.part2 import solve as part2_solve
from utils import get_data_path


class TestPart1:
    def test_example(self):
        result = part1_solve(get_data_path(__file__, 'example.txt'))
        assert result == 15

    def test_input(self):
        result = part1_solve(get_data_path(__file__, 'input.txt'))
        assert result == 11063


class TestPart2:
    def test_example(self):
        result = part2_solve(get_data_path(__file__, 'example.txt'))
        assert result == 12

    def test_input(self):
        result = part2_solve(get_data_path(__file__, 'input.txt'))
        assert result == 10349
