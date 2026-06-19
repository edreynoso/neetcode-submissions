class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next= next

class LinkedList:
    
    def __init__(self):
        self.head = None

    
    def get(self, index: int) -> int:

        if self.head is None:
            return -1
        
        i = 0

        curr = self.head

        while curr and i <= index:
            if i == index:
                return curr.val
            curr = curr.next
            i +=1
        
        return -1

    def insertHead(self, val: int) -> None:

        if self.head is None:
            self.head = Node(val)
            return

        curr = self.head

        new_head = Node(val)

        self.head = new_head
        self.head.next = curr

    def insertTail(self, val: int) -> None:

        if self.head is None:
            self.head = Node(val)
            return
        
        curr = self.head

        while curr.next:
            curr = curr.next

        curr.next = Node(val)
        

    def remove(self, index: int) -> bool:

        if self.head is None or index < 0:
            return False

        if index == 0:
            self.head = self.head.next
            return True
        
        curr = self.head
        
        prev = None

        i = 0

        while curr and i <= index:
            if i == index:
                prev.next = curr.next
                
                print(self.head.val)
                return True
            i +=1
            prev = curr
            curr = curr.next

        return False
        

    def getValues(self) -> List[int]:

        values = []

        curr = self.head

        while curr:

            values.append(curr.val)
            curr = curr.next


        return values
        
