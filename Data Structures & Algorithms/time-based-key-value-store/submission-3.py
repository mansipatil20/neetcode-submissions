class TimeMap:

    def __init__(self):
        # Dictionary to store key → list of (timestamp, value)
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        result = ""
        left = 0
        arr = self.store[key]
        right = len(arr)-1
        while left <= right:
            mid = (left+right) //2
            if arr[mid][0] <= timestamp:
                result = arr[mid][1]
                left = mid +1
            else:
                right = mid -1

        return result
        # for t, v in self.store[key]:
        #     if t <= timestamp:
        #         result = v  # update result if timestamp is valid
        #     else:
        #         break  # since timestamps are increasing, stop early
        # return result