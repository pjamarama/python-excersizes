h_window = 1.5

def bouncingBall(h, bounce, window):
    number = 0
    if h > 0 and 0 < bounce < 1 and window < h:
        while h > window:
            h *= bounce
            number += 1
        return number * 2 - 1
    return -1

print (bouncingBall(20, 0.66, 1.5))
print( bouncingBall(-20, 0.66, 1.5))
print( bouncingBall(20, 1.66, 1.5))
print( bouncingBall(20, 0.66, 115))