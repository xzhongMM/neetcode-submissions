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
            if(nums.isEmpty()){
                nums.push(i);
                System.out.println("pushed " + i + " onto stack");
                continue;
            }

            while(!(nums.isEmpty())){
                int prevIndex = nums.peek();
                int prev = temperatures[prevIndex];
                if(currentTemp > prev){
                    System.out.println("encounter warmer temp: " + currentTemp + " > " + prev);
                    daysBefore[nums.peek()] = i - prevIndex;
                    nums.pop();
                    System.out.println("popped " + prev + " ffrom stack");
                }
                else{
                    System.out.println(currentTemp + " is smaller than " + prev + ", do nothing");
                    break;
                }
            }

            nums.push(i);
            System.out.println("push " + currentTemp + " onto stack");
        }

        return daysBefore;
    }
}
