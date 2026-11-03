class LRUCache:
    def __init__(self, capacity: int):
        self.cache_memory = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache_memory:
            value = self.cache_memory.pop(key)
            self.cache_memory[key] = value
            return self.cache_memory[key]
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache_memory:
            self.cache_memory.pop(key)
            self.cache_memory[key] = value
        elif len(self.cache_memory) < self.capacity:
            self.cache_memory[key] = value
        else:
            # remove 1st ele
            first_key = next(iter(self.cache_memory))
            self.cache_memory.pop(first_key)
            self.cache_memory[key] = value
            
        
        
