class Solution {
    public String largestNumber(int[] nums) {

        String[] arr = new String[nums.length];

    
        for (int i = 0; i < nums.length; i++) arr[i] = "" + nums[i];
        
        for (int i = 0; i < arr.length - 1; i++) {

            boolean swapped = false;

            for (int j = 0; j < arr.length - i - 1; j++) {

                String first = arr[j] + arr[j + 1];
                String second = arr[j + 1] + arr[j];

                if (first.compareTo(second) < 0) {
                    String temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }

            if (!swapped) break;
        }

        
        if (arr[0].equals("0")) return "0";

        String ans = "";

        for (int i = 0; i < arr.length; i++) ans += arr[i];

        return ans;
    }
}
