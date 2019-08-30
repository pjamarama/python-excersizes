def tower_builder(n_floors):
    floor = [[" "] * (2 * n_floors - 1)] * n_floors
    
    x = 2 * n_floors - 1
    y = (x - 1) // 2
    
    floor[0][y] = "*"

    for i in range(1, n_floors):
        floor[i][y-i] = "*"
        floor[i][y+i] = "*"

    return floor

tower = tower_builder(4)

for flo in tower:
    print(flo)
