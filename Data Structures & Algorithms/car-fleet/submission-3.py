class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        total_fleet = 0
        map_dict = sorted(zip(position, speed), key=lambda x: x[0], reverse = True)
        fleet_stack = -1
        
        for i in range(len(map_dict)):
            arrival_time = (target - map_dict[i][0])/map_dict[i][1]
            if fleet_stack == -1:
                total_fleet += 1
                fleet_stack = (arrival_time)
            else:
                if arrival_time > fleet_stack:
                    total_fleet +=1
                    fleet_stack = arrival_time

        
        return total_fleet
        