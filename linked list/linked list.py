class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index):
        if index >= self.length or index < 0:
            return -1
        else:
            count = 0
            current_node = self.head
            while count != index:
                current_node = current_node.next
                count += 1
            return current_node.val

    def add_at_head(self, val):
        node = Node(val)
        self.length += 1
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def add_at_tail(self, val):
        node = Node(val)
        self.length += 1
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = node

    def add_at_index(self, index, val):
        if index == 0:
            self.add_at_head(val)
        elif index == self.length:
            self.add_at_tail(val)
        elif index < self.length:
            previous_node = self.head
            current_node = self.head.next
            count = 1
            while count < index:
                previous_node = current_node
                current_node = current_node.next
                count += 1
            node = Node(val)
            self.length += 1
            previous_node.next = node
            node.next = current_node

    def delete_at_index(self, index):
        if self.length < index >= 0:
            self.length -= 1
            if index == 0:
                self.head = self.head.next
            else:
                previous_node = self.head
                current_node = self.head.next
                count = 1
                while count < index:
                    previous_node = current_node
                    current_node = current_node.next
                    count += 1
                previous_node.next = current_node.next

    def print_linked_list(self):
        current_node = self.head
        while current_node:
            print(current_node.val, end='')
            current_node = current_node.next

    def fill_linked_list(self):
        current_node = self.head
        result = ''
        while current_node:
            result += current_node
            current_node = current_node.next
        return result

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.val
            current = current.next


def main():
    lst = MyLinkedList()
    lst.add_at_tail(3)
    lst.add_at_tail(5)
    lst.add_at_tail(7)
    for num in lst:
        print(num)


if __name__ == "__main__":
    main()
