from three_Sum import Solution
import pytest

@pytest.mark.report_tracemalloc
@pytest.mark.report_duration
@pytest.mark.parametrize("expected,test_input", [([[-1,-1,2],[-1,0,1]],[-1,0,1,2,-1,-4]), ([],[0,1,1]),([[0,0,0]],[0,0,0])])
def test_1(expected,test_input):
    answer = Solution()
    assert answer.Sum3_neat(test_input) == expected