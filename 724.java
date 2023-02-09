class Solution {
    public int pivotIndex(int[] nums) {
        nums = runningSum(nums);
        if (nums[nums.length-1] - nums[0] == 0){
            return 0; 
        }

        for (int i =1;i<nums.length-1;i++){ 
            if (i != 0 && i != nums.length-1 &&nums[i-1] == nums[nums.length-1] - nums[i]){
                return i;
            }
        }
        if (nums[nums.length - 2] == 0){
            return nums.length-1;
        }
        return -1; 
    }
    public int[] runningSum(int[] nums) {
        int x = 0;
        for (int i=0; i < nums.length; i++){
            x += nums[i];
            nums[i] = x;
        }
        return nums;
    }
}