def nqueen(n):
    columns = set()
    diag_down = set() # (r - c)
    diag_up = set()  # (r + c)

    result = []

    board = [["."]*n for i in range(n)]

    def backtrack(row):
        if row == n:
            copy = [''.join(r) for r in board]
            result.append(copy)
            return
        for column in range(n):
            if column in columns or (row + column) in diag_up or (row-column) in diag_down:
                continue
            else:
                columns.add(column)
                diag_down.add(row-column)
                diag_up.add(row+column)
                board[row][column] = "Q"
                backtrack(row + 1)


                columns.remove(column)
                diag_down.remove(row-column)
                diag_up.remove(row+column)
                board[row][column] = "."
    backtrack(0)
    return result



    [
    [
        ".Q..",
        "...Q",
        "Q...",
        "..Q."
    ],



    ["..Q.","Q...","...Q",".Q.."]]