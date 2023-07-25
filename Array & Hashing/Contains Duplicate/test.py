from contains_duplicate import Solution
import pytest

@pytest.mark.report_tracemalloc
@pytest.mark.report_duration
@pytest.mark.parametrize("expected,test_input", [(True,[1,2,3,1]), (False,[1,2,3,4]),(True,[1,1,1,3,3,4,3,2,4,2])])
def test_1(expected,test_input):
    answer = Solution()
    assert answer.containsDuplicate_SS(test_input) == expected