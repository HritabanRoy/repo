def bouncing_ball(h, bounce, window):
    count = 1
    if h > 0 and bounce > 0 and bounce < 1 and window < h:
        while window < h:
            h = h * bounce
            if window < h:
                count = count + 2
            print(h)
        return count
    else:
        return -1

print(bouncing_ball(3, 0.66, 1.5))