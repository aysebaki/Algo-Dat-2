class ChainingHashNode():
    def __init__(self, key=None):
        self.key = key
        self.next = None

class ChainingHashSet():
    def __init__(self, capacity=0):
        self.hash_table = [None] * capacity
        self.table_size = 0
        self.capacity = capacity

    def get_hash_code(self, key):
        """Hash function that calculates a hash code for a given key using the modulo division.
        :param key:
        		Key for which a hash code shall be calculated according to the length of the hash table.
        :return:
        		The calculated hash code for the given key.

        """
        if key is None:
            raise ValueError("Key cannot be None")
        return key % self.capacity

    def get_hash_table(self):
        """(Required for testing only)
        :return the hash table.
        """
        return self.hash_table

    def set_hash_table(self, table):
        """(Required for testing only) Set a given hash table..
        :param table: Given hash table which shall be used.

        !!!
        Since this method is needed for testing we decided to implement it.
        You do not need to change or add anything.
        !!!

        """
        self.hash_table = table
        self.capacity = len(table)
        self.table_size = 0
        for node in table:
            while node is not None:
                self.table_size += 1
                node = node.next

    def get_table_size(self):
        """returns the number of stored keys (keys must be unique!)."""
        return self.table_size

    def insert(self, key):
        """Inserts a key and returns True if it was successful. If there is already an entry with the
          same key, the new key will not be inserted and False is returned.
         :param key:
         		The key which shall be stored in the hash table.
         :return:
         		True if key could be inserted, or False if the key is already in the hash table.
         :raises:
         		a ValueError if any of the input parameters is None.
         """
        if key is None:
            raise ValueError("Key cannot be None")

        hash_code = self.get_hash_code(key)
        node = self.hash_table[hash_code]

        while node is not None:
            if node.key == key:
                return False  # Key already exists
            node = node.next

        new_node = ChainingHashNode(key)
        new_node.next = self.hash_table[hash_code]
        self.hash_table[hash_code] = new_node
        self.table_size += 1
        return True

    def contains(self, key):
        """Searches for a given key in the hash table.
         :param key:
         	    The key to be searched in the hash table.
         :return:
         	    True if the key is already stored, otherwise False.
         :raises:
         	    a ValueError if the key is None.
         """
        if key is None:
            raise ValueError("Key cannot be None")

        hash_code = self.get_hash_code(key)
        node = self.hash_table[hash_code]

        while node is not None:
            if node.key == key:
                return True
            node = node.next

        return False

    def remove(self, key):
        """Removes the key from the hash table and returns True on success, False otherwise.
        :param key:
        		The key to be removed from the hash table.
        :return:
        		True if the key was found and removed, False otherwise.
        :raises:
         	a ValueError if the key is None.
        """
        if key is None:
            raise ValueError("Key cannot be None")

        hash_code = self.get_hash_code(key)
        node = self.hash_table[hash_code]
        prev_node = None

        while node is not None:
            if node.key == key:
                if prev_node is None:
                    self.hash_table[hash_code] = node.next
                else:
                    prev_node.next = node.next
                self.table_size -= 1
                return True  # Key removed
            prev_node = node
            node = node.next

        return False  # Key not found

    def clear(self):
        """Removes all stored elements from the hash table by setting all nodes to None.
        """
        self.hash_table = [None] * self.capacity
        self.table_size = 0

    def to_string(self):
        """Returns a string representation of the hash table (array indices and stored keys) in the format
            Idx_0 {Node, Node, ... }, Idx_1 {...}
            e.g.: 0 {13}, 1 {82, 92, 12}, 2 {2, 32}, """
        result = []
        for idx, node in enumerate(self.hash_table):
            key_list = []
            while node is not None:
                key_list.append(str(node.key))
                node = node.next
            result.append(f"{idx} {{{', '.join(key_list)}}}")

        return ', '.join(result)
