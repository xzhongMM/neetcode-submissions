class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int l = temperatures.length;
        Stack<Integer> nums = new Stack<>();
        int[] daysBefore = new int[l];
        for(int i = 0; i<l; i++){
            daysBefore[i] = 0;
        }

        for(int i = 0; i<l; i++){
            int currentTemp = temperatures[i];
            System.out.println("processing " + currentTemp);

            while(!(nums.isEmpty()) && (currentTemp > temperatures[nums.peek()])){
                int prevIndex = nums.pop();
                daysBefore[prevIndex] = i - prevIndex;
            }

            nums.push(i);
            System.out.println("push " + currentTemp + " onto stack");
        }

        return daysBefore;
    }
}
