class MinStack:

    def __init__(self):
        self.stack = dict()
        self.top_key = -1
        self.min_ = None

    def push(self, val: int) -> None:
        self.top_key += 1
        self.stack[self.top_key] = (val, self.min_)
        if self.min_ is not None:
            if self.min_ >= val:
                self.min_ = val
        else:
            self.min_ = val

    def pop(self) -> None:
        if self.top_key != -1:
            deleted_item = self.stack.pop(self.top_key)
            self.top_key -= 1
        if self.top_key != -1:
            if deleted_item[0] == self.min_:
                self.min_ = deleted_item[1]
        else:
            self.min_ = None
    
    def top(self) -> int:
        if self.top_key != -1:
            return self.stack[self.top_key][0]

    def getMin(self) -> int | None:
        return self.min_
