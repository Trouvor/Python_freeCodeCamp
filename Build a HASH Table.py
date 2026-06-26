class HashTable:
    def __init__(self):
        self.collection = dict()

    def add(self, key, value):
        hash_key = self.hash(key)

        if hash_key not in self.collection:
            self.collection[hash_key] = {}

        self.collection[hash_key][key] = value

    def remove(self, key):
        hash_key = self.hash(key)
        
        if hash_key in self.collection:
            bucket = self.collection[hash_key]

            if key in bucket:
                del bucket[key]
            
            if not bucket:
                del self.collection[hash_key]

    
    def lookup(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection:
            bucket = self.collection[hash_key]
            return bucket.get(key)

        return None


    def hash(self, key):
        sum = 0
        for chr in key:
            sum += ord(chr)            
        return sum 