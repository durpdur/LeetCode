/* 
    Following solution is O(n^2)
    
    Explanation:
    * (first n) Selects a value in the array, then iterates through the rest of the array.
        * (second n) Repeat for every value in the array.

*/

class ContainsDuplicateBruteForce {
    public static boolean containsDuplicate(int[] nums) {
        for (int i = 0; i < nums.length - 1; i++) { // first loop: selecting a value with first pointer
            for (int j = i + 1; j < nums.length; j++) { // second loop: checking the rest of the array starting from
                if (nums[i] == nums[j]) { // If the value is equal, its a duplicate
                    return true;
                }
            }
        }
        return false; // once all values are looped through, and no duplicates are found, return false
    }

    public static void main(String args[]) {
        int[] nums = { 1, 1, 1, 3, 3, 4, 3, 2, 4, 2 };

        System.out.println(containsDuplicate(nums));
    }
}