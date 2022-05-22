states = ["Lagos", "Sokoto"]
Dict = {(states[0], states[1]): 2}


def dis(start, end):
    n, time_taken = 0, 0
    route = ""
    state = start
    while n < len(Dict):
        key = Dict.keys()
        key = list(key)
        if (state == key[n][0]) & (state != end):
            curr = key[n]
            route += state + ", "
            time_taken += Dict.get(curr)
            state = key[n][1]
        else:
            n += 1
            continue
    sent = "The route taken is " + route + "The time taken is " + str(time_taken) + "Their positions are " \
           + str(states.index(start)) + " and " + str(states.index(end))
    return sent

print(dis("Lagos", "Sokoto"))
        
