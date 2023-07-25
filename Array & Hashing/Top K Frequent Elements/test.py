from top_k_frequent_elements import Solution
import pytest

@pytest.mark.report_tracemalloc
@pytest.mark.report_duration
@pytest.mark.parametrize("expected,test_input", [([1,2],([1,1,1,2,2,3],2)), ([1],([1],1)), ([1,2],([1,2,1,2,1,3],2)), ([1,2],([1,2,3,4,5,6],2))])
def test(expected,test_input):
    answer = Solution()
    assert answer.top_k_frequent_elements_neat(test_input[0],test_input[1]) == expected