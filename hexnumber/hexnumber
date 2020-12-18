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

    def __add__(self, reversed_linked_num):
        if type(reversed_linked_num) != MyLinkedList:
            return
        result = ''
        mem_rank = 0
        current_node_num1 = self.head
        current_node_num2 = reversed_linked_num.head
        while current_node_num1 or current_node_num2:
            if not current_node_num1:
                current_node_num1 = Node('0')
            if not current_node_num2:
                current_node_num2 = Node('0')
            result_sum = hex_dictionary[current_node_num1.val] + hex_dictionary[current_node_num2.val] + mem_rank
            if result_sum > 15:
                mem_rank = 1
                result_sum -= 16
            else:
                mem_rank = 0
            for key, value in hex_dictionary.items():
                if value == result_sum:
                    result += key
            current_node_num1 = current_node_num1.next
            current_node_num2 = current_node_num2.next
        if mem_rank == 1:
            result += str(mem_rank)
        return MyLinkedList(result)


def check_number(num):
    if '-' not in num:
        for symbol in set(num):
            if symbol.islower():
                return False
            if symbol not in hex_dictionary:
                return False
        return True
    else:
        return False


def check_nulls(num):
    if len(num.lstrip('0')) == 0:
        return '0'
    else:
        return num.lstrip('0')


hex_dictionary = dict([('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8),
                           ('9', 9), ('A', 10), ('B', 11), ('C', 12), ('D', 13), ('E', 14), ('F', 15)])


def main():
    num1 = check_nulls(input())
    num2 = check_nulls(input())
    linked_num1 = MyLinkedList(num1)
    linked_num2 = MyLinkedList(num2)
    if check_number(num1) and check_number(num2):
        (linked_num1 + linked_num2).print_linked_list()
    else:
        print('Error')


if __name__ == "__main__":
    main()
