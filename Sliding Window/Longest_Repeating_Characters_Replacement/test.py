from Longest_Repeating_Characters_Replacement import Solution
import pytest

@pytest.mark.report_tracemalloc
@pytest.mark.report_duration
@pytest.mark.parametrize("expected,test_input", [(4,["ABAB",2]), (4,["AABABBA",1])])
def test_1(expected,test_input):
    answer = Solution()
    assert answer.Longest_Repeating_Characters_Replacement_SS(test_input[0],test_input[1]) == expected