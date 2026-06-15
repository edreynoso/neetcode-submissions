class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        
        int result[] = new int[temperatures.length];

        Deque<Integer> stack = new ArrayDeque();


        for (int n = temperatures.length -1; n >= 0; n--){

            while (stack.size() > 0 && temperatures[stack.peek()] <= temperatures[n]){
                stack.pop();
            }
            
            if (stack.size() == 0){
                result[n] = 0;
            }else{
                result[n] = stack.peek() -n;
            }
            stack.push(n);
        }

        return result;
    }
}
