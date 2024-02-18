def get_people_who_know_secret(n, intervals, first_person):
    knows_secret = [False] * n
    knows_secret[first_person] = True
    for interval in intervals:
        if any(knows_secret[interval[0]:interval[1]+1]):
            for j in range(interval[0], interval[1]+1):
                knows_secret[j] = True
    result = [i for i, knows in enumerate(knows_secret) if knows]
    return result

n = 5
intervals = [[0, 2], [1, 3], [2, 4]]
first_person = 0
result = get_people_who_know_secret(n, intervals, first_person)
print(result)

