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


print(func_ops(180, DATOS.TEMPERATURA.BAJA, DATOS.TEMPERATURA.VALORES))
print(func_ops(8.5, DATOS.TIEMPO.POCO, DATOS.TIEMPO.VALORES))
print(func_ops(2, DATOS.NIVEL_PIZZA.POCO_COCINADA, DATOS.NIVEL_PIZZA.VALORES))

