class MyHashMap:

    def __init__(self):
        self.key=0
        self.value=0
        self.lst=[]

    def put(self, key: int, value: int) -> None:
        if len(self.lst)<1:
            self.lst.append([key,value])
            return
        flag=1
        for i in range(len(self.lst)):
            if self.lst[i][0] == key:
                self.lst[i][1]=value
                falg=0
                return
        if flag:
            self.lst.append([key,value])

    def get(self, key: int) -> int:
        flag=1
        for i in range(len(self.lst)):
            if self.lst[i][0] == key:
                falg=0
                return self.lst[i][1]
        if flag:
            return -1

    def remove(self, key: int) -> None:
        i = 0
        while i < len(self.lst):
            if self.lst[i][0] == key:
                del self.lst[i]
            else:
                i += 1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)