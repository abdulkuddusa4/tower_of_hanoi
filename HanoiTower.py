class ColorBar:
    def __init__(self,size,color):
        self.size=size
        self.color=color

    def __gt__(self, other):
        return True if self.size>other.size else False

    def __lt__(self, other):
        return True if self.size<other.size else False

    def __eq__(self, other):
        return True if self.size==other.data else False
    def __repr__(self):
        return str(self.size)






class HanoiStackNode:
    def __init__(self,bar):
        self.bar = bar
        self.next = None

    def __lt__(self, other):
        return True if self.bar<other.bar else False

    def __gt__(self, other):
        return True if self.bar>other.bar else False


class HanoiStack:
    def __init__(self):
        self.head = None
        self.__length = 0

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.bar
            cur = cur.next

    def __len__(self):
        return self.__length

    def push(self, bar):
        if type(bar) != ColorBar:
            print(bar)
            # exit()
            raise TypeError(f"object {bar} must be a {ColorBar} not {type(bar)}")
        if self.head is None:
            self.head = HanoiStackNode(bar)
            self.__length+=1
        else:
            cur = self.head
            new = HanoiStackNode(bar)
            if cur>new:
                new.next = cur
                self.head = new
                self.__length+=1
            else:
                raise ValueError(f"bar size must be greater than{cur.bar}")

    def pop(self):
        if self.head is None:
            raise IndexError("stack is empty")
        else:
            cur = self.head
            self.head = cur.next
            self.__length-=1
            return cur.bar

def play():pass
