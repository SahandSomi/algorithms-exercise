from Permutation_in_String import Solution
import pytest

@pytest.mark.report_tracemalloc
@pytest.mark.report_duration
@pytest.mark.parametrize("expected,test_input", [(True,["ab","eidbaooo"]), (False,["ab","eidboaoo"])])
def test_1(expected,test_input):
    answer = Solution()
    assert answer.Permutation_in_String_SS(test_input[0],test_input[1]) == expected