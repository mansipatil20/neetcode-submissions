class TimeMap:

    def __init__(self):
        # Dictionary to store key → list of (timestamp, value)
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If key not present, initialize with empty list
        if key not in self.store:
            self.store[key] = []
        # Append the new (timestamp, value) pair
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # If key not present, return empty string
        if key not in self.store:
            return ""
        
        # Scan through all values for this key
        result = ""
        for t, v in self.store[key]:
            if t <= timestamp:
                result = v  # update result if timestamp is valid
            else:
                break  # since timestamps are increasing, stop early
        return result

