
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def mirror(head):
    resp_head = None
    front = head
    back_node = None
    front_node = None
    unlinked_node = None
    while front:
        if back_node is None:
            back_node = Node(front.data)
            front_node = back_node
            unlinked_node = front_node
            front = front.next
            continue
        if front.data == " ":
            unlinked_node.next = Node(" ")
            unlinked_node = unlinked_node.next
            if resp_head is None:
                resp_head = back_node
            else:
                unlinked_node.next = back_node
                unlinked_node = front_node
            if front.next:
                back_node = Node(front.next.data)
                front_node = back_node
                front = front.next.next
            else:
                front = front.next
            continue
        temp_node = Node(front.data)
        temp_node.next = back_node
        back_node = temp_node
        front = front.next
    if resp_head is None:
        resp_head = back_node
    else:
        unlinked_node.next = back_node
    return resp_head

def print_list(head):
    while head:
        print head.data
        head = head.next

head = Node("H")
head.next = Node("e")
head.next.next = Node("l")
head.next.next.next = Node("l")
head.next.next.next.next = Node("o")
head.next.next.next.next.next = Node(" ")
head.next.next.next.next.next.next = Node("W")
head.next.next.next.next.next.next.next = Node("o")
head.next.next.next.next.next.next.next.next = Node("r")
head.next.next.next.next.next.next.next.next.next = Node("l")
head.next.next.next.next.next.next.next.next.next.next = Node("d")
print_list(head)
print "--"
print_list(mirror(head))

