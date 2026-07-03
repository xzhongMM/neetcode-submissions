class Solution {
    public boolean isValid(String s) {
        Stack<Character> charStack = new Stack<>();
        char[] chars = s.toCharArray();

        for(char c : chars){
            if(c == '('){
                charStack.push('(');
            }
            else if(c == '{'){
                charStack.push('{');
            }
            else if(c == '['){
                charStack.push('[');
            }
            else if(c == ')'){
                if(charStack.empty()){
                    return false;
                }
                else if(charStack.pop() != '('){
                    return false;
                }
            }
            else if(c == '}'){
                if(charStack.empty()){
                    return false;
                }
                else if(charStack.pop() != '{'){
                    return false;
                }
            }
            else if(c == ']'){
                if(charStack.empty()){
                    return false;
                }
                else if(charStack.pop() != '['){
                    return false;
                }
            }
        }

        if(charStack.empty()){
            return true;
        }
        else{
            return false;
        }
    }
}
