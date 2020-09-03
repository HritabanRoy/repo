def make_readable(seconds):
    time = ['', '', '']
    seconds = min(seconds, 359999)
    for i in range(3):
        r = seconds % (60) if i < 2 else seconds
        time[i] = str(r) if r > 9 else '0' + str(r)
        seconds = int(seconds / (60))
    time.reverse()
    return ':'.join(time)

print(make_readable(359999))