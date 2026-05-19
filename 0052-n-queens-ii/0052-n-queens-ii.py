class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()       # occupied columns
        diag1 = set()      # row - col
        diag2 = set()      # row + col
        
        self.count = 0

        def backtrack(row):
            # If all queens are placed
            if row == n:
                self.count += 1
                return

            for col in range(n):
                # Check if position is safe
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                # Place queen
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # Move to next row
                backtrack(row + 1)

                # Remove queen (backtrack)
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return self.count