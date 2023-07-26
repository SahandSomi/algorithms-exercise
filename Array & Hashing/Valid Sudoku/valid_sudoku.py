import collections

class Solution(object):

    def valid_sudoku_SS(self, board:list)-> bool:

        # check row
        for row in board:
            check_dict = {}
            for i in row:
                if i!="." and i not in check_dict:
                    check_dict[i] = check_dict.get(i,0) + 1
                elif i in check_dict:
                    return False
        
        # check column
        for colidx in range(9):
            check_dict = {}
            for rowidx in range(9):
                if board[rowidx][colidx] != "." and board[rowidx][colidx] not in check_dict:
                    check_dict[board[rowidx][colidx]] = check_dict.get(board[rowidx][colidx],0) + 1

                elif board[rowidx][colidx] in check_dict:
                    return False
                
        # check 3*3
        for rowidx in range(0,7,3):
            for colidx in range(7):
                check_dict = {}
                for step in range(3):
                    list_3 = [board[rowidx+step][colidx], board[rowidx+step][colidx+1], board[rowidx+step][colidx+2]]
                    for number in list_3:
                        if number !="." and number not in check_dict:
                            check_dict[number] = check_dict.get(number,0) + 1
                        elif number in check_dict:
                            return False
                        
        
        return True


    def valid_sudoku_neat(self, board:list)-> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True



# Guide for solution:

# Hash Map: time complexity O(9**2) and space O(9**2)

### Golden rule: Hash Set to check for duplication, Hashing 3*3 by dict and value is going to be hash set. key(r/3,c/3)