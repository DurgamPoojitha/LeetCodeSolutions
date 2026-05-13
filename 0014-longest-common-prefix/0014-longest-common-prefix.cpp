class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        
        // Start with first string as prefix
        string prefix = strs[0];
        
        // Compare prefix with remaining strings
        for(int i = 1; i < strs.size(); i++) {
            
            // Reduce prefix until it matches
            while(strs[i].find(prefix) != 0) {
                prefix.pop_back();
                
                // If prefix becomes empty
                if(prefix.empty()) {
                    return "";
                }
            }
        }
        
        return prefix;
    }
};