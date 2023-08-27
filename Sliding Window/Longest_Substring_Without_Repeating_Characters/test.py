from Longest_Substring_Without_Repeating_Characters import Solution
import pytest

@pytest.mark.report_tracemalloc
@pytest.mark.report_duration
@pytest.mark.parametrize("expected,test_input", [(3,"abcabcbb"), (1,"bbbbb"), (3,"pwwkew")])
def test_1(expected,test_input):
    answer = Solution()
    assert answer.Longest_Substring_Without_Repeating_Characters_SS(test_input) == expected