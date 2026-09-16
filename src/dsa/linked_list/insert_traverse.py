from asyncio.windows_events import NULL


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next!= None:
                temp = temp.next

            temp.next = new_node


    def traverse(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next



o = LinkedList()
o.insert_at_end(1)
o.insert_at_end(2)
o.insert_at_end(3)
o.insert_at_end(4)
o.traverse()
