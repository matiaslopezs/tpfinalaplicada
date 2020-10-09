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


print(tiempo(8.5, 'mucho'))
