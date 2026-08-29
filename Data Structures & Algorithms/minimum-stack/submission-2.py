class MinStack:

    def __init__(self):
        self.list = []
        self.minList = []

    def push(self, val: int) -> None:
        self.list.append(val)
        if not self.minList:
            self.minList.append(val)
        elif self.minList[-1] >= val:
            self.minList.append(val)

    def pop(self) -> None:
        if self.minList[-1] == self.list[-1]:
            del self.minList[-1]
        del self.list[-1]

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return self.minList[-1]
        
