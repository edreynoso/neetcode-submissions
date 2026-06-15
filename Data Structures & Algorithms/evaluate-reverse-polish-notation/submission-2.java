class Solution {
    public int evalRPN(String[] tokens) {
        
        Deque<Integer> stack = new ArrayDeque();
        Queue<Integer> queue = new LinkedList();

        int total = 0;

        if (tokens.length ==1 ) return Integer.parseInt(tokens[0]);

        for (String s: tokens){

            try {
                stack.push(Integer.parseInt(s));
            }
            catch(NumberFormatException e){
                int op2 = stack.pop();
                int op1 = stack.pop();


                switch(s){
                    case "+":
                        total = op1 + op2;
                        break;
                    case "-": 
                        total = op1 - op2;
                        break;
                    case "*":
                        total = op1 * op2;
                        break;
                    case "/":
                        total = op1 / op2;
                        break;
                }
                stack.push(total);
            }

        }

        return total;
    }
}
