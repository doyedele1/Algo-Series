'''
    Explanation:
        Use two stacks: stack and minStack. minStack stores the minimum of each value in the stack
        Pop, top and getMin must not be called on empty stacks
        TC: O(1) for all operations, SC: O(n)
'''

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack: val = min(val, self.minStack[-1])
        else: val = val
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()