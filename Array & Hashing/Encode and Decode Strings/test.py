from encode_and_decode_strings import Solution
import pytest

@pytest.mark.report_tracemalloc
@pytest.mark.report_duration
@pytest.mark.parametrize("expected,test_input", [("lint:;code:;love:;you",["lint","code","love","you"]), ("we:;say:;:::;yes",["we", "say", ":", "yes"])])
def test_encode(expected,test_input):
    answer = Solution()
    assert answer.encode_strings_SS(test_input) == expected




@pytest.mark.report_tracemalloc
@pytest.mark.report_duration
@pytest.mark.parametrize("test_input,expected", [("lint:;code:;love:;you",["lint","code","love","you"]), ("we:;say:;:::;yes",["we", "say", ":", "yes"])])
def test_decode(expected,test_input):
    answer = Solution()
    assert answer.decode_strings_SS(test_input) == expected