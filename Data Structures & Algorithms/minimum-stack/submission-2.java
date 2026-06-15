class MinStack {

    Deque<Integer> stack;
    Deque<Integer> min;
    public MinStack() {
        this.stack = new ArrayDeque<>();
        this.min = new ArrayDeque<>();
    }
    
    public void push(int val) {
        if (this.min.peek() == null  || this.min.peek() >= val){
            this.min.push(val);
        }

        this.stack.push(val);
    }
    
    public void pop() {
        int val = stack.pop();

        if (this.min.peek() != null && this.min.peek() == val) this.min.pop();
    }
    
    public int top() {
        return this.stack.peek();
    }
    
    public int getMin() {
        if (this.min.peek() != null){
            return this.min.peek();
        }
        return 0;
    }
}
