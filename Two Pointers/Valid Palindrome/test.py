from valid_palindrome import Solution
import pytest

@pytest.mark.report_tracemalloc
@pytest.mark.report_duration
@pytest.mark.parametrize("expected,test_input", [(True,"A man, a plan, a canal: Panama"), (False,"race a car"),(True," ")])
def test_1(expected,test_input):
    answer = Solution()
    assert answer.valid_palindrome_SS(test_input) == expected