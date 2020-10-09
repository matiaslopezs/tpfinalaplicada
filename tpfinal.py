class DATOS:
    class TEMPERATURA:
        BAJA = 'baja'
        ALTA = 'alta'
        VALORES = {
            'baja': [160, 200],
            'alta': [180, 230]
        }
    class TIEMPO:
        POCO = 'poco'
        MUCHO = 'mucho'
        VALORES = {
            'poco': [5, 12],
            'mucho': [10, 20]
        }
    class NIVEL_PIZZA:
        POCO_COCINADA = 'poco cocinada'
        EN_SU_PUNTO = 'en su punto'
        MUY_COCINADA = 'muy cocinada'
        VALORES = {
            'poco cocinada': [0, 4],
            'en su punto': [3, 7],
            'muy cocinada': [6, 10],
        }


def func_ops(x, subconjunto, datos):
    temps = datos[subconjunto]
    mid = (temps[0] + temps[1]) / 2
    return (x - temps[0]) / (mid - temps[0]) if temps[0] <= x < mid else (temps[1] - x) / (temps[1] - mid) if mid <= x < temps[1] else 0


func_ops(180, DATOS.TEMPERATURA.BAJA, DATOS.TEMPERATURA.VALORES)
func_ops(8.5, DATOS.TIEMPO.POCO, DATOS.TIEMPO.VALORES)


"""
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
"""


#print(tiempo(8.5, 'mucho'))
