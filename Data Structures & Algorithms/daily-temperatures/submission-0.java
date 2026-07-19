class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int l = temperatures.length;
        Stack<Integer> nums = new Stack<>();
        boolean[] hasBig = new boolean[l];
        for(int i = 0; i<l; i++){
            hasBig[i] = false;
        }
        int[] daysBefore = new int[l];
        for(int i = 0; i<l; i++){
            daysBefore[i] = 0;
        }

        for(int i = 0; i<l; i++){
            int currentTemp = temperatures[i];
            System.out.println("processing " + currentTemp);
            if(nums.isEmpty()){
                nums.push(currentTemp);
                System.out.println("pushed " + currentTemp + " onto stack");
                continue;
            }

            for(int j = 0; j<i; j++){
                if(!(hasBig[j])){
                    daysBefore[j]++;
                    System.out.println("incrementing index " + j + "'s daysBefore to " + daysBefore[j]);
                }
            }

            while(!(nums.isEmpty())){
                int prev = nums.peek();
                if(currentTemp > prev){
                    System.out.println("encounter warmer temp: " + currentTemp + " > " + prev);
                    for(int k = i-1; k>=0; k--){
                        if(!(hasBig[k])){
                            hasBig[k] = true;
                            System.out.println("set index " + k + " to true");
                            break;
                        }
                    }
                    nums.pop();
                    System.out.println("popped " + prev + " ffrom stack");
                }
                else{
                    System.out.println(currentTemp + " is smaller than " + prev + ", do nothing");
                    break;
                }
            }

            nums.push(currentTemp);
            System.out.println("push " + currentTemp + " onto stack");
        }

        for(int j = 0; j<l; j++){
            if(!(hasBig[j])){
                daysBefore[j] = 0;
            }
        }

        return daysBefore;
    }
}
