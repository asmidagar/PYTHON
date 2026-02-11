class Node:
    def __init__(self, data = None):
        self.Data = data
        self.Next = None

class SLL:
    def __init__(self):
        self.start = None

    def insert_at_start(self, data):
        t = Node(data)
        t.Next = self.start
        self.start = t

    def insert_at_end(self, data):
        pass
    def insert_at_after(self, data):
        pass

    def delete_at_start(self):
        if(self.start == None):
            print("List is empty")
        else:
            self.start = self.start.Next

    def delete_at_end(self):
        pass
    def delete_at_after(self):
        pass
    def printAll(self):
        temp = self.start
        while temp:
            print(temp.Data, end = " ")
            temp = temp.Next
        print()

    def search(self, data):
        t = self.start
        while t:
            if(t.Data == data):
                return True
            t = t.Next
        return False
    
obj1 = SLL()
obj1.insert_at_start(10)
obj1.insert_at_start(20)
obj1.delete_at_start()
obj1.insert_at_start(30)
obj1.insert_at_start(40)
obj1.insert_at_start(50)
obj1.insert_at_start(60)

obj1.printAll()

print(obj1.search(30))