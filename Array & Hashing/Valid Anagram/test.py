from valid_anagram import Solution
import pytest

@pytest.mark.report_tracemalloc
@pytest.mark.report_duration
@pytest.mark.parametrize("expected,test_input", [(True,["anagram","nagaram"]), (False,["rat","car"])])
def test(expected,test_input):
    answer = Solution()
    assert answer.valid_anagram_SS(test_input[0],test_input[1]) == expected