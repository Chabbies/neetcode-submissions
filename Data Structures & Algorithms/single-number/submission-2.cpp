class Solution {
public:
    int singleNumber(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int i = 0;
        while (i < (nums.size()-1)){
            if (nums[i] == nums[i+1] && i != (nums.size()-2)){
                i += 2;
            }
            else{
                return nums[i];
            }
        }
        return nums[i];
    };
};
