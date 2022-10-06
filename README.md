# Postfix calculator
Postfix notation is a way of expressing mathematical operations which eliminates the need for brackets. This is done by putting the operator AFTER the operands.

 ## Example:
 Prefix (conventional) operation:
 (3+5)*2=16
 Notice how brackets are needed to give the order of operation.

 Postfix:
 3 5 + 2 * = 16
 By putting the operators after the operands, brackets are no longer needed.

 # Script Explanation
 Input: A string, space separated, a postfix expression.
 Output: Result of postfix expression

 Process: Push operands onto a stack. If operator detected, operate on two most recent operands. Push result onto stack.