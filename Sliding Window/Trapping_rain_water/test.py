from Trapping_rain_water import Solution
import pytest

@pytest.mark.report_tracemalloc
@pytest.mark.report_duration
@pytest.mark.parametrize("expected,test_input", [(6,[0,1,0,2,1,0,1,3,2,1,2,1]), (9,[4,2,0,3,2,5]),(10,[4,2,0,3,2,4,3,4]),(83,[6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3])])
def test_1(expected,test_input):
    answer = Solution()
    assert answer.Trapping_rain_water_SS(test_input) == expected