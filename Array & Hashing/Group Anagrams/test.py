from group_anagrams import Solution
import pytest

@pytest.mark.report_tracemalloc
@pytest.mark.report_duration
@pytest.mark.parametrize("expected,test_input", [([["eat","tea","ate"],["tan","nat"],["bat"]],["eat","tea","tan","ate","nat","bat"]), ([[""]],[""]),([["a"]],["a"])])
def test(expected,test_input):
    answer = Solution()
    assert answer.group_anagrams_SS(test_input) == expected