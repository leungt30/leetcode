class Solution {
    public int search(int[] nums, int target) {
        int hi = nums.length-1;
        int low = 0;
        int med = (hi+low) / 2;

        while (low <= hi){
            med = (hi+low) / 2;
            if (nums[med] == target){
                return med;
            }
            else if (nums[med] > target){
                hi = med-1;
            }
            else{
                low = med+1;
            }
        }
        return -1;

    }
}