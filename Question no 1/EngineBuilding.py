import heapq

def min_build_time(engines, split_time):
    engine_queue = list(engines)
    heapq.heapify(engine_queue)
    
    while len(engine_queue) > 1:
        fastest_engine = heapq.heappop(engine_queue)
        second_fastest_engine = heapq.heappop(engine_queue)
        heapq.heappush(engine_queue, second_fastest_engine + split_time)
    
    return heapq.heappop(engine_queue)

if __name__ == "__main__":
    engines = [5, 3, 7, 2, 8]
    split_time = 4
    total_time = min_build_time(engines, split_time)
    print(f"Minimum time to build all engines: {total_time}")

