class MyLinkedListNode:
    
    def __init__(self, val=None):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head=None
        
    def __len__(self):
        c = self.head
        i = 0
        if c != None:
            while c.next != None:
                i += 1
                c = c.next
            if c.val != None:
                i += 1
        return i
    
    def lookAll(self, ll) -> str:
        c = ll.head
        s = ''
        l = len(self)
        for i in range(l):
            s += f'[{i}={c.val}],'
            c = c.next
        return s

    def get(self, index: int) -> int:
        # print(f'GET {index} from {self.lookAll(self)}')
        c = self.head
        l = len(self)
        if index < 0 or index > l - 1:
            return -1
        if index == 0:
            return c.val
        for i in range(index):
            c = c.next
        return c.val

    def addAtHead(self, val: int) -> None:
        # print(f'ADD {val} at Head {self.lookAll(self)}')
        cs = self.head
        c = MyLinkedListNode(val)
        if cs != None:
            c.next = cs
        self.head = c
        # print(f'{self.lookAll(self)}')

    def addAtTail(self, val: int) -> None:
        # print(f'ADD {val} at Tail {self.lookAll(self)}')
        cn = MyLinkedListNode(val)
        c = self.head
        if c != None:
            i = 1
            l = len(self)
            while i < l:
                c = c.next
                i += 1
            c.next = cn
        else:
            self.head = cn
        # print(f'{self.lookAll(self)}')

    def addAtIndex(self, index: int, val: int) -> None:
        # print(f'ADD {val} at index {index} to {self.lookAll(self)}')
        if index == 0:
            self.addAtHead(val)
        else:
            l = len(self)
            if index == l:
                self.addAtTail(val)
            else:
                if index > 0 and index < l:
                    c = MyLinkedListNode(val)
                    cp = self.head
                    cn = self.head
                    cn = cn.next
                    i = 1
                    while i < index:
                        cp = cp.next
                        cn = cn.next
                        i += 1
                    c.next = cn
                    cp.next = c
        # print(f'{self.lookAll(self)}')
            

    def deleteAtIndex(self, index: int) -> None:
        # print(f'DELETE from index {index} from {self.lookAll(self)}')
        if index == 0:
            self.head = self.head.next
        else:
            l = len(self)
            if index == l - 1:
                cn = self.head
                while cn.next.next != None:
                    cn = cn.next
                cn.next = None
            else:
                if index > 0 and index < l - 1:
                    cp = self.head
                    cn = self.head
                    cn = cn.next
                    cn = cn.next
                    i = 1
                    while i < index:
                        cn = cn.next
                        cp = cp.next
                        i += 1
                    cp.next = cn
        # print(f'{self.lookAll(self)}')
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)