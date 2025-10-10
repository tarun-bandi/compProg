class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        busstop_to_route_nums = collections.defaultdict(list)

        for route_num, route in enumerate(routes):
            for stop in route:
                busstop_to_route_nums[stop].append(route_num)
        
        queue = collections.deque()
        visited_stops = set()

        for stop in busstop_to_route_nums[source]:
            queue.append(stop)
            visited_stops.add(stop)

        count = 1
        while queue:
            
            for _ in range(len(queue)): # Empty the queue
                route = queue.popleft()

                for stop in routes[route]:
                    if stop == target:
                        return count 
                    
                    for route in busstop_to_route_nums[stop]:
                        if route not in visited_stops:
                            visited_stops.add(route)
                            queue.append(route)
            count += 1
        
        return -1



        
        
