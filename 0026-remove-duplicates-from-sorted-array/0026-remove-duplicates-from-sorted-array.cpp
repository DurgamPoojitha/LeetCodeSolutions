#include <vector>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {

        // Pointer for unique elements
        int k = 1;

        for (int i = 1; i < nums.size(); i++) {

            // If current element is different
            if (nums[i] != nums[i - 1]) {
                nums[k] = nums[i];
                k++;
            }
        }

        return k;
    }
};