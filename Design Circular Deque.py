class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = []
        self.length = k
        

    def insertFront(self, value: int) -> bool:
        if len(self.queue) < self.length: 
            self.queue.insert(0,value)
            #print(self.queue)
            return True
        return False
        
        

    def insertLast(self, value: int) -> bool:
        if len(self.queue) < self.length: 
            self.queue.append(value)
            #print(self.queue)
            return True
        return False

    def deleteFront(self) -> bool:
        if len(self.queue) > 0: 
            del self.queue[0]
            #print(self.queue)
            return True
        return False
        

    def deleteLast(self) -> bool:
        if len(self.queue) > 0: 
            self.queue.pop()
            #print(self.queue)
            return True
        return False
        

    def getFront(self) -> int:
        if len(self.queue) > 0: 
            #print(self.queue)
            return self.queue[0]
        return -1
        

    def getRear(self) -> int:
        if len(self.queue) > 0: 
            #print(self.queue)
            return self.queue[len(self.queue)-1]
        return -1
        

    def isEmpty(self) -> bool:
        if len(self.queue)  == 0:
            return True
        return False
        

    def isFull(self) -> bool:
        if len(self.queue) == self.length:
            return True
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
