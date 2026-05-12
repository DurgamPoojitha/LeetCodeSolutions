class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        vector<int> lastIndex(256, -1);

        int left = 0;
        int maxLen = 0;

        for (int right = 0; right < s.size(); right++) {

            // If character already exists in current window
            if (lastIndex[s[right]] >= left) {
                left = lastIndex[s[right]] + 1;
            }

            // Update last seen index
            lastIndex[s[right]] = right;

            // Update maximum length
            maxLen = max(maxLen, right - left + 1);
        }

        return maxLen;
    }
};