class Contact:
    def __init__(self, name: str, number: str):
        self.name = name
        self.number = number
    def __str__(self) -> str:
        return f"{self.name}: {self.number}"


class Node:
    def __init__(self, key: str, value: Contact):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size: int):
        self.size = size
        self.data = [None] * size
    def hash_function(self, key: str) -> int:
        # Simple hash: sum of character codes modulo table size
        return sum(ord(c) for c in key) % self.size
    def insert(self, key: str, number: str):
        index = self.hash_function(key)
        new_contact = Contact(key, number)
        new_node = Node(key, new_contact)
        if self.data[index] is None:
            self.data[index] = new_node
        else:
            current = self.data[index]
            while current:
                if current.key == key:
                    # Update existing contact
                    current.value = new_contact
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node
    def search(self, key: str):
        index = self.hash_function(key)
        current = self.data[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    def print_table(self):
        for i, node in enumerate(self.data):
            print(f"Index {i}:", end=" ")
            if not node:
                print("Empty")
            else:
                current = node
                while current:
                    print(f"- {current.value}", end=" ")
                    current = current.next
                print()

"""
A hash table is the perfect fit for a contact manager that needs to find information fast. By turning each contact’s name into a numeric index using a hash function, we can store and retrieve data in almost constant time — way faster than searching through a list or walking a tree.

To deal with collisions, I used separate chaining. Each spot in the table holds a linked list of Node objects. If two contacts end up at the same index, they just get added to the chain. When I search or insert, the program only looks through that small list, so everything stays efficient and accurate even with overlaps.

An engineer would pick a hash table over a list when the dataset is big and quick lookups are the priority — like in contact apps, caches, or dictionaries. Compared to a tree, hash tables use less structure and tend to run faster on average, though trees keep everything sorted. For this project, the hash table design keeps things simple, lightweight, and really fast for adding, updating, or finding contacts.
"""
