class Solution {
public:
    vector<vector<char>> rotateTheBox(vector<vector<char>>& boxGrid) {
        int m = boxGrid.size();
        int n = boxGrid[0].size();

        // Step 1: Simulate gravity in each row
        for (int i = 0; i < m; i++) {
            int emptyPos = n - 1;

            for (int j = n - 1; j >= 0; j--) {

                // Obstacle resets position
                if (boxGrid[i][j] == '*') {
                    emptyPos = j - 1;
                }

                // Move stone to the farthest possible position
                else if (boxGrid[i][j] == '#') {
                    swap(boxGrid[i][j], boxGrid[i][emptyPos]);
                    emptyPos--;
                }
            }
        }

        // Step 2: Rotate matrix 90 degrees clockwise
        vector<vector<char>> result(n, vector<char>(m));

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                result[j][m - 1 - i] = boxGrid[i][j];
            }
        }

        return result;
    }
};