def temperatura(x, subconjunto):
    if subconjunto == 'baja':
        if 160 <= x < 180:
            return (x - 160) / (180 - 160)
        elif 180 <= x < 200:
            return (200 - x) / (200 - 180)
    elif subconjunto == 'alta':
        if 180 <= x < 205:
            return (x - 180) / (205 - 180)
        elif 205 <= x < 230:
            return (230 - x) / (230 - 205)
    return 0


def tiempo(x, subconjunto):
    if subconjunto == 'poco':
        if 5 <= x < 8.5:
            return (x - 5) / (8.5 - 5)
        elif 8.5 <= x < 12:
            return (12 - x) / (12 - 8.5)
    elif subconjunto == 'mucho':
        if 10 <= x < 15:
            return (x - 10) / (15 - 10)
        elif 15 <= x < 20:
            return (20 - x) / (20 - 15)
    return 0


def nivel_pizza(x, subconjunto):
    if subconjunto == 'poco cocinada':
        if 0 <= x < 2:
            return (x - 0) / (2 - 0)
        elif 2 <= x < 4:
            return (4 - x) / (4 - 2)
    elif subconjunto == 'en su punto':
        if 3 <= x < 5:
            return (x - 3) / (5 - 3)
        elif 5 <= x < 7:
            return (7 - x) / (7 - 5)
    elif subconjunto == 'muy cocinada':
        if 6 <= x < 8:
            return (x - 6) / (8 - 6)
        elif 8 <= x < 10:
            return (10 - x) / (10 - 8)
    return 0


print(tiempo(8.5, 'mucho'))
