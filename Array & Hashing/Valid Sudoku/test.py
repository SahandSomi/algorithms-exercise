from valid_sudoku import Solution
import pytest

@pytest.mark.report_tracemalloc
@pytest.mark.report_duration
@pytest.mark.parametrize("expected,test_input", [(True,[["5","3",".",".","7",".",".",".","."]
                                                        ,["6",".",".","1","9","5",".",".","."]
                                                        ,[".","9","8",".",".",".",".","6","."]
                                                        ,["8",".",".",".","6",".",".",".","3"]
                                                        ,["4",".",".","8",".","3",".",".","1"]
                                                        ,["7",".",".",".","2",".",".",".","6"]
                                                        ,[".","6",".",".",".",".","2","8","."]
                                                        ,[".",".",".","4","1","9",".",".","5"]
                                                        ,[".",".",".",".","8",".",".","7","9"]]), (False,[["8","3",".",".","7",".",".",".","."]
                                                                                                        ,["6",".",".","1","9","5",".",".","."]
                                                                                                        ,[".","9","8",".",".",".",".","6","."]
                                                                                                        ,["8",".",".",".","6",".",".",".","3"]
                                                                                                        ,["4",".",".","8",".","3",".",".","1"]
                                                                                                        ,["7",".",".",".","2",".",".",".","6"]
                                                                                                        ,[".","6",".",".",".",".","2","8","."]
                                                                                                        ,[".",".",".","4","1","9",".",".","5"]
                                                                                                        ,[".",".",".",".","8",".",".","7","9"]])])
def test(expected,test_input):
    answer = Solution()
    assert answer.valid_sudoku_SS(test_input) == expected