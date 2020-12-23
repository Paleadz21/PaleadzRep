class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        cur = self.head
        while cur:
            print(cur.data, end=' ')
            cur = cur.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_between_node(self, prev_node, data):
        if not prev_node:
            print('Previous node does not exist!')
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, data):
        cur = self.head
        if cur.data == data:
            self.head = cur.next
            cur = None
            return

        prev = None
        while cur and cur.data != data:
            prev = cur
            cur = cur.next

        if not cur:
            return

        prev.next = cur.next
        cur = None

    def length(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def swap_node(self, node_1, node_2):
        if node_1 == node_2:
            return

        cur_1 = self.head
        prev_1 = None
        while cur_1 and cur_1.data != node_1:
            prev_1 = cur_1
            cur_1 = cur_1.next

        cur_2 = self.head
        prev_2 = None
        while cur_2 and cur_2.data != node_2:
            prev_2 = cur_2
            cur_2 = cur_2.next

        if not cur_1 and not cur_2:
            return

        if prev_1:
            prev_1.next = cur_2
        else:
            self.head = cur_2

        if prev_2:
            prev_2.next = cur_1
        else:
            self.head = cur_1

        cur_1.next, cur_2.next = cur_2.next, cur_1.next

    def reverse_list(self):
        cur = self.head
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def merge_two_lists(self, llist):
        list_1 = self.head
        list_2 = llist.head
        merged_list = []

        if not list_1:
            return list_2
        if not list_2:
            return list_1

        if list_1 and list_2:
            if list_1.data <= list_2.data:
                merged_list = list_1
                list_1 = merged_list.next
            else:
                merged_list = list_2
                list_2 = merged_list.next
            new_head = merged_list

        while list_1 and list_2:
            if list_1.data <= list_2.data:
                merged_list.next = list_1
                merged_list = list_1
                list_1 = merged_list.next
            else:
                merged_list.next = list_2
                merged_list = list_2
                list_2 = merged_list.next

            if not list_1:
                merged_list.next = list_2
            if not list_2:
                merged_list.next = list_1

    def remove_dup(self):
        cur = self.head
        prev = None
        dup_values = []
        while cur:
            if cur.data in dup_values:
                prev.next = cur.next
            else:
                dup_values.append(cur.data)
                prev = cur
            cur = cur.next

    def nth_to_last_node(self, n):
        length = self.length()
        cur = self.head
        while cur:
            if length == n:
                print(cur.data)
            length -= 1
            cur = cur.next

    def move_tail_to_head(self):
        cur = self.head
        prev = None
        while cur.next:
            prev = cur
            cur = cur.next
        cur.next = self.head
        self.head = cur
        prev.next = None


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.move_tail_to_head()
print(ll.head.data)
ll.print()
