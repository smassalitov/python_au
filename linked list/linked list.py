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

    def __init__(self, string):
        self.head = None
        self.length = 0
        for i in range(len(string)):
            self.add_at_head(string[i])

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
            yield current.value
        current = current.next

    def __add__(self, reversed_linked_num):
        if type(reversed_linked_num) != MyLinkedList:
            return
        result = ''
        current_node_num1 = self.head
        current_node_num2 = reversed_linked_num.head
        while current_node_num1:
            if not current_node_num1.next:
                current_node_num1.next = current_node_num2
                return current_node_num1
            current_node_num1.next


def main():
    num = input()
    lst = MyLinkedList(num)
    lst.print_linked_list()


if __name__ == "__main__":
    main()
