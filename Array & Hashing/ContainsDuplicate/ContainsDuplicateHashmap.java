import java.util.HashMap;

/* Explanation:
 * (first n) iterates through the array
 *      * checks if the number is already in the HashMap
 *      * if not, put() it into the HashMap (All hashmap operations are O(1) if not collision)
 */

class ContainsDuplicateHashMap {
    public static boolean containsDuplicates(int[] nums) {
        HashMap<Integer, Integer> numsMap = new HashMap<>();
        for (int n : nums) {
            /*
             * Checks if map conatins key
             * then checks if key has been seen once or more
             */
            if (numsMap.containsKey(n) && numsMap.get(n) >= 1) {
                return true;
            } else {
                /*
                 * getOrDefault returns the value of the first parameter
                 * 
                 * If map does not contain the value, the HashMap gets updated with the value
                 * and the number of times it was seen
                 */
                numsMap.put(n, numsMap.getOrDefault(n, 0) + 1);
            }
        }
        return false; // Once all nums has been looped through and no dups are found return false
    }

    public static void main(String args[]) {
        int[] nums = { 1, 1, 1, 3, 3, 4, 3, 2, 4, 2 };

        System.out.println(containsDuplicates(nums));
    }
}