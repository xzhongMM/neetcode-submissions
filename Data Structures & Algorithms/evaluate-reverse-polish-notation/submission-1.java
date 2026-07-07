class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> operands = new Stack<>();

        for(String token : tokens){
            if(token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/")){
                if(operands.size() >= 2){
                    int operand2 = operands.pop();
                    int operand1 = operands.pop();
                    switch(token){
                        case "+":
                            operands.push(operand1 + operand2);
                            break;
                        case "-":
                            operands.push(operand1 - operand2);
                            break;
                        case "*":
                            operands.push(operand1 * operand2);
                            break;
                        case "/":
                            operands.push(operand1 / operand2);
                            break;
                    }
                }
                else{
                    return -1;
                }
            }
            else{
                operands.push(Integer.parseInt(token));
            }
        }

        if(operands.size() == 1){
            return operands.pop();
        }
        return -1;
    }
}
