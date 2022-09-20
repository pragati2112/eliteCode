class HashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = [[], ] * self.size

    def set_val(self, key, val):
        bucket_idx = hash(key) % self.size
        bucket = self.hash_table[bucket_idx]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                found_key = True
                break

        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))

    def get_val(self, key):

        bucket_idx = hash(key) % self.size
        bucket = self.hash_table[bucket_idx]

        for index, record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                return record_val
                break

        return 'No record found'

    def remove_val(self, key):
        bucket_idx = hash(key) % self.size
        bucket = self.hash_table[bucket_idx]

        for index, record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                bucket.pop(index)
                break


myHashTable = HashTable(10)

myHashTable.set_val('123', 'apple')
myHashTable.set_val('456', 'banana')
myHashTable.set_val('789', 'mango')

print(myHashTable.get_val('123'))
