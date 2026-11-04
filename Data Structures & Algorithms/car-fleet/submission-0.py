class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        total_fleet = 0
        map_dict = {}
        fleet_stack = []
        for p in range(len(position)):
            map_dict[position[p]] = speed[p]
        
        new_list = sorted(map_dict.items(), reverse = True)
        for i in range(len(new_list)):
            arrival_time = (target - new_list[i][0])/new_list[i][1]
            if not fleet_stack:
                fleet_stack.append(arrival_time)
            else:
                if arrival_time > fleet_stack[-1]:
                    fleet_stack.append(arrival_time)

        while fleet_stack:
            fleet_stack.pop()
            total_fleet += 1
        
        return total_fleet
        