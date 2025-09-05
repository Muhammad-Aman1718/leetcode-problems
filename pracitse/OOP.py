# class Solution:
#     def check_elements(self, a: list[int], d:int):
#         # Your code goes here
#         # arr.sort()
#         # count = 0
#         # for i in b:
#         #     if i in a:
#         #         count += 1
#         #         a.remove(i)

#         # if count == len(b):
#         #     return True
#         # return False


#         for i in d:
#             arr.insert(len(arr), )


# obj = Solution()
# a = [11, 7, 1, 13, 21, 3, 7, 3]
# # a = [1, 2, 3]
# b = [11, 3, 7, 1, 7]
# # b = [1, 1]


# arr = [-1, -2, -3, 4, 5, 6, 7]
# d = 2
# print(obj.check_elements(arr, b))


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # Empty buckets
        self.count = 0

    def hash_function(self, key):
        """Simple hash function using division method"""
        return key % self.size

    def insert(self, key):
        """Insert a key into hash table"""
        hash_index = self.hash_function(key)
        bucket = self.table[hash_index]

        # Check if key already exists
        if key not in bucket:
            bucket.append(key)
            self.count += 1
            print(f"Inserted {key} at index {hash_index}")
        else:
            print(f"{key} already exists at index {hash_index}")

    def search(self, key):
        """Search for a key in hash table"""
        hash_index = self.hash_function(key)
        bucket = self.table[hash_index]

        if key in bucket:
            print(f"Found {key} at index {hash_index}")
            return True
        else:
            print(f"{key} not found")
            return False

    def display_table(self):
        """Display the complete hash table"""
        print("\n" + "=" * 50)
        print("HASH TABLE STRUCTURE")
        print("=" * 50)
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")
        print(f"\nTotal elements: {self.count}")
        print(f"Load factor: {self.count/self.size:.2f}")
        print("=" * 50)

    def show_hash_calculations(self, values):
        """Show hash calculations for each value"""
        print("\nHASH CALCULATIONS:")
        print("-" * 30)
        for value in values:
            hash_val = self.hash_function(value)
            print(f"{value} % {self.size} = {hash_val}")


# Your values
my_values = [1, 6, 232, 1, 5, 5, 76, 34632, 5762343, 2, 89, 345, 2, 8943, 45]

print("Original Values:", my_values)

# Create hash table with size 10
ht = HashTable(10)

# Show hash calculations first
ht.show_hash_calculations(my_values)

print("\n" + "=" * 50)
print("INSERTING VALUES INTO HASH TABLE")
print("=" * 50)

# Insert all values
for value in my_values:
    ht.insert(value)

# Display final table structure
ht.display_table()

print("\n" + "=" * 50)
print("SEARCHING FOR VALUES")
print("=" * 50)

# Search for some values
search_values = [1, 232, 999, 45, 100]
for value in search_values:
    ht.search(value)

print("\n" + "=" * 50)
print("COLLISION ANALYSIS")
print("=" * 50)

# Analyze collisions
collision_count = 0
for i, bucket in enumerate(ht.table):
    if len(bucket) > 1:
        collision_count += len(bucket) - 1
        print(f"Index {i}: {len(bucket)} values = {bucket} (COLLISION!)")
    elif len(bucket) == 1:
        print(f"Index {i}: {len(bucket)} value = {bucket}")
    else:
        print(f"Index {i}: Empty")

print(f"\nTotal collisions: {collision_count}")

# Memory analysis
print("\n" + "=" * 50)
print("MEMORY ANALYSIS")
print("=" * 50)

unique_values = list(set(my_values))
print(f"Original values: {len(my_values)} (with duplicates)")
print(f"Unique values stored: {len(unique_values)}")
print(f"Table size: {ht.size} buckets")
print(f"Memory efficiency: {len(unique_values)/ht.size*100:.1f}% filled")

# Show alternative table size
print("\n" + "=" * 30)
print("TRYING WITH LARGER TABLE SIZE")
print("=" * 30)

# Create larger hash table for better distribution
ht_large = HashTable(20)
print(f"\nWith table size {ht_large.size}:")

for value in unique_values:
    hash_val = ht_large.hash_function(value)
    ht_large.insert(value)

ht_large.display_table()

# Performance comparison
print("\n" + "=" * 50)
print("PERFORMANCE COMPARISON")
print("=" * 50)


def count_collisions(hash_table):
    collisions = 0
    for bucket in hash_table.table:
        if len(bucket) > 1:
            collisions += len(bucket) - 1
    return collisions


small_collisions = count_collisions(ht)
large_collisions = count_collisions(ht_large)

print(f"Table size 10: {small_collisions} collisions")
print(f"Table size 20: {large_collisions} collisions")
print(f"Collision reduction: {small_collisions - large_collisions}")

# Show how retrieval works
print("\n" + "=" * 50)
print("RETRIEVAL PROCESS EXAMPLE")
print("=" * 50)


def detailed_search(hash_table, key):
    print(f"\nSearching for {key}:")
    print(
        f"Step 1: Calculate hash = {key} % {hash_table.size} = {hash_table.hash_function(key)}"
    )

    hash_index = hash_table.hash_function(key)
    bucket = hash_table.table[hash_index]

    print(f"Step 2: Check bucket at index {hash_index}: {bucket}")

    if key in bucket:
        position = bucket.index(key)
        print(f"Step 3: Found {key} at position {position} in bucket")
        print(f"Result: SUCCESS - Found in O(1) average time")
    else:
        print(f"Step 3: {key} not found in bucket")
        print(f"Result: NOT FOUND")


# Demonstrate detailed search
detailed_search(ht, 232)
detailed_search(ht, 999)
