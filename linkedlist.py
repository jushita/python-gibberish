class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elements = list()
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elements.append(cur.data)
        print(elements)

    def get(self, index):
        if index >= self.length():
            print("Error: 'Get' index out of range")
            return None
        cur_index = 0
        cur = self.head
        while True:
            cur = cur.next
            if cur_index == index:
                return cur.data
            cur_index += 1

    def erase(self,index):
        if index >= self.length():
            print ("ERROR")
            return
        cur_idx = 0
        cur = self.head
        while True:
            last_node = cur
            cur = cur.next
            if cur_idx == index:
                last_node.next = cur.next
                return
            cur_idx += 1


mylist = linked_list()

mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)

mylist.display()
mylist.erase(0)
mylist.display()
