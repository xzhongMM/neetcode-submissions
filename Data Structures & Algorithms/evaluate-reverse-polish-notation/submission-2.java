class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> operands = new Stack<>();

        for(String token : tokens){
            switch(token){
                case "+":
                    operands.push(operands.pop() + operands.pop());
                    break;
                case "-":
                    int operand2 = operands.pop();
                    int operand1 = operands.pop();
                    operands.push(operand1 - operand2);
                    break;
                case "*":
                    operands.push(operands.pop() * operands.pop());
                    break;
                case "/":
                    operand2 = operands.pop();
                    operand1 = operands.pop();
                    operands.push(operand1 / operand2);
                    break;
                default:
                    operands.push(Integer.parseInt(token));
                    break;
            }
        }

        return operands.peek();
    }
}
