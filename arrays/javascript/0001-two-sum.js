/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let map = {}
    for(let i=0;i<nums.length;i++) {
        let value = nums[i]
        let complement_value = target - value
        if(map[complement_value] !== undefined) {
            return [i,map[complement_value]]
        } else {
            map[value] = i
        }
    }
};