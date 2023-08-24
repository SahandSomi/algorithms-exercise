from Trapping_rain_water import Solution
import pytest

@pytest.mark.report_tracemalloc
@pytest.mark.report_duration
@pytest.mark.parametrize("expected,test_input", [(6,[0,1,0,2,1,0,1,3,2,1,2,1]), (9,[4,2,0,3,2,5]),(0,[0,4,1,0])])
def test_1(expected,test_input):
    answer = Solution()
    assert answer.Trapping_rain_water_SS(test_input) == expected