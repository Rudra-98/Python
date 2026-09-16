from asyncio.windows_events import NULL


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data,self.head)
        self.head = new_node

    def traverse(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

    def get_size(self):
        temp = self.head
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        print(count)


    def remove_at_index(self, index):
        temp = self.head
        count = 1
        while count < index:
            count += 1
            temp = temp.next
        temp.next = temp.next.next


    def insert_at_index(self, index, data):
        temp = self.head
        count = 1
        while count < index:
            count += 1
            temp = temp.next
        data = Node(data, temp.next)
        temp.next = data


o = LinkedList()
o.insert_at_end(1)
o.insert_at_end(2)
o.insert_at_end(4)
o.insert_at_end(5)
# o.traverse()
# o.get_size()
# o.remove_at_index(2)
# o.traverse()
o.insert_at_index(2,3)
o.traverse()
