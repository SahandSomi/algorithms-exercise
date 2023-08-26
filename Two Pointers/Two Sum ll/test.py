from two_sum_2 import Solution
import pytest

@pytest.mark.report_tracemalloc
@pytest.mark.report_duration
@pytest.mark.parametrize("expected,test_input", [([1,2],[[2,7,11,15],9]), ([1,3],[[2,3,4],6]),([1,2],[[-1,0],-1]),([3,4],[[1,3,4,5,7,10,11],9])])
def test_1(expected,test_input):
    answer = Solution()
    assert answer.two_sum_2_neat(test_input[0],target=test_input[1]) == expected