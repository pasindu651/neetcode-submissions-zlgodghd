class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const seen = {}
        for(let i = 0; i < nums.length; i++) {
            let y = target - nums[i];
            if(y in seen) {
                return [seen[y], i];
            }
            seen[nums[i]] = i;
        }
    }
}
