class MinStack:
    _minstack: list
    _stack: list
    def __init__(self):
        self._minstack = list()
        self._stack = list()

    def push(self, val: int) -> None:
        self._stack.append(val)
        if not self._minstack or val <= self._minstack[-1]:
            self._minstack.append(val)

    def pop(self) -> None:
        item = self._stack.pop()
        if item == self._minstack[-1]:
            self._minstack.pop()
        return item

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()