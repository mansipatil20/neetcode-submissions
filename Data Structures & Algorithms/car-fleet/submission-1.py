class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        total_fleet = 0
        # map_dict = zip(position, speeed)
        map_dict = sorted(zip(position, speed), key=lambda x: x[0], reverse = True)
        fleet_stack = []
        
        # new_list = sorted(map_dict.items(), reverse = True)
        for i in range(len(map_dict)):
            arrival_time = (target - map_dict[i][0])/map_dict[i][1]
            if not fleet_stack:
                fleet_stack.append(arrival_time)
            else:
                if arrival_time > fleet_stack[-1]:
                    fleet_stack.append(arrival_time)

        while fleet_stack:
            fleet_stack.pop()
            total_fleet += 1
        
        return total_fleet
        