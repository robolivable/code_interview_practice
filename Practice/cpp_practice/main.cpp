
#include <iostream>

struct Node {
	int data;
	Node *next = NULL;
	Node(const int d) { data = d; }
};

Node *insert (Node *head, int data) {
	Node *front = head;
	while (true) {
		if (!front->next)
			break;
		front = front->next;
	}
	front->next = new Node(data);
	return head;
}

Node *insert_nth (Node *head, int data, int pos) {
	Node *node = new Node(data);
	if (!head) {
		return node;
	}
	if (pos == 0) {
		node->next = head;
		head = node;
		return head;
	}
	Node *front = head->next;
	Node *prev = head;
	for (int i = 1; i < pos; ++i) {
		if (!front || !front->next)
			break;
		front = front->next;
		prev = prev->next;
	}
	node->next = front;
	prev->next = node;
	return head;
}

void print_list (Node *head) {
	while (true) {
		if (!head)
			break;
		std::cout << head->data << "\n";
		if (!head->next)
			break;
		head = head->next;
	}
}

int main (int argc, const char *argv[]) {
	Node *head = NULL;
	print_list(head);
	std::cout << "\n";

	head = insert_nth(head, 3, 0);
	print_list(head);
	std::cout << "\n";

	head = insert_nth(head, 5, 1);
	print_list(head);
	std::cout << "\n";

	head = insert_nth(head, 4, 2);
	print_list(head);
	std::cout << "\n";

	head = insert_nth(head, 2, 3);
	print_list(head);
	std::cout << "\n";

	head = insert_nth(head, 10, 1);
	print_list(head);
	std::cout << "\n";
}
