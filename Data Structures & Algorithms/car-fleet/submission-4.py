class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        total_fleet = 0
        map_dict = sorted(zip(position, speed), key=lambda x: x[0], reverse = True)
        highest_time = -1
        
        for i in range(len(map_dict)):
            arrival_time = (target - map_dict[i][0])/map_dict[i][1]
            if highest_time == -1:
                total_fleet += 1
                highest_time = (arrival_time)
            else:
                if arrival_time > highest_time:
                    total_fleet +=1
                    highest_time = arrival_time

        
        return total_fleet
        