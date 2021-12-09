class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return reduce(operator.mul,[ (lambda x : len(list(filter(lambda a: a != ".", x))) == 
                                      len(set(filter(lambda a: a != ".", x)))) (foo(i)) 
                                      for foo in [ lambda index: board[index],
                                                 lambda index: [row[index] for row in board],
                                                 lambda index: 
                                                    board[0+3*(index//3)][0+3*(index%3):3+3*(index%3)]+
                                                    board[1+3*(index//3)][0+3*(index%3):3+3*(index%3)]+
                                                    board[2+3*(index//3)][0+3*(index%3):3+3*(index%3)]
                                               ] for i in range(0,9)])
