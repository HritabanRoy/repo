def is_valid_walk(walk):
    if len(walk) == 10 and walk.count('n')==walk.count('s') and walk.count('w')==walk.count('e'):
        return True
    else:
        return False
