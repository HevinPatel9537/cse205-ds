class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) 
    {vector<vector<int>> result = {{}};
    for (int num : nums) {
        int n = result.size();
        for (int i = 0; i < n; i++) {
            result.push_back(result[i]);
            result.back().push_back(num);
        }
    }
    return result;
} 
};