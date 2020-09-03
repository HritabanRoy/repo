def josephus_survivor(n,k):
    #soln seen
    v = 0
    for i in range(1, n + 1):
        v = (v + k) % i
    return v + 1



def josephus_survivor2(n,k):
    soldiers = [int(i) for i in range(1, n + 1)]
    counter = -1
    while len(soldiers) != 1:
        counter += k
        while counter >= len(soldiers):
            counter = abs(len(soldiers) - counter)
        soldiers.remove(soldiers[counter])
        counter -= 1
    return soldiers[0]

print(josephus_survivor(11,19))