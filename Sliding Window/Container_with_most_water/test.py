from Container_with_most_water import Solution
import pytest

@pytest.mark.report_tracemalloc
@pytest.mark.report_duration
@pytest.mark.parametrize("expected,test_input", [(49,[1,8,6,2,5,4,8,3,7]), (1,[1,1]),(100,[1,100,100,2,5,4,8,3,7])])
def test_1(expected,test_input):
    answer = Solution()
    assert answer.Container_with_most_water_SS(test_input) == expected