class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Linked:
    def __init__(self):
        self.start = None

    def display(self):
        print("[", end="")
        if self.start:
            print(self.start.value, end="")
            current = self.start.next
            while current:
                print(", ", end="")
                print(current.value, end="")
                current = current.next
        print("]")

    def insert(self, index, value):
        if index == 0:
            self.start = Node(value, self.start)
        else:
            current = self.start
            count = 1

            while count < index:
                current = current.next
                count += 1

            current.next = Node(value, current.next)

    def delete(self, index):
        if index == 0:
            self.start = self.start.next
        else:
            current = self.start
            count = 1

            while count < index:
                current = current.next
                count += 1

            current.next = current.next.next

    def getValue(self, index):
        curr = self.start
        while index > 0:
            curr = curr.next
            index -= 1
        return curr.value

    def append(self, value):
        if self.start == None:
            self.start = Node(value)
        else:
            current = self.start
            while current.next != None:
                current = current.next
            current.next = Node(value)

    def isEmpty(self):
        return (self.start == None)

    def length(self):
        if self.start == None:
            return 0
        else:
            curr = self.start
            count = 1
            while curr.next != None:
                curr = curr.next
                count += 1
            return count

    def sum(self):
        result = 0

        for i in range(self.length()):
            result += self.getValue(i)
        return result

    def delete_all(self, value):
        i = 0

        while i < self.length():
            if self.getValue(i) == value:
                self.delete(i)
            else:
                i += 1

    def reverse(self):
        previous = None
        current = self.start

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.start = previous
        
# Done with the help of Walter Barr
    def split(self, condition):
        other = Linked()
        kept_tail = None
        other_tail = None
        current = self.start
        self.start = None

        while current is not None:
            next_node = current.next
            current.next = None

            if condition(current.value):
                if kept_tail is None:
                    self.start = current
                else:
                    kept_tail.next = current

                kept_tail = current
            else:
                if other_tail is None:
                    other.start = current
                else:
                    other_tail.next = current

                other_tail = current

            current = next_node

        return other