class MinStack {
    Stack<Integer> mainStack;
    Stack<Integer> mins;

    public MinStack() {
        mainStack = new Stack<>();
        mins = new Stack<>();
    }
    
    public void push(int val) {
        mainStack.push(val);
        if(mins.isEmpty()){
            mins.push(val);
        }
        else{
            mins.push(Math.min(val, mins.peek()));
        }
    }
    
    public void pop() {
        mainStack.pop();
        mins.pop();
    }
    
    public int top() {
        return mainStack.peek();
    }
    
    public int getMin() {
        return mins.peek();
    }
}
