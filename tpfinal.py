import sys
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
def calcular_reglas(temperatura, tiempo):
    """
    REGLAS:
    1) Si la Temperatura es Baja y el Tiempo es Mucho entonces la Pizza estará En su punto. 
    2) Si la Temperatura es Baja y el Tiempo es Poco entonces la Pizza estará Poco hecha. 
    3) Si la Temperatura es Alta y el Tiempo es Mucho entonces la Pizza estará Muy hecha. 
    4) Si la Temperatura es Alta y el Tiempo es Poco entonces la Pizza estará En su punto. 
    """
    if( temperatura == DATOS.TEMPERATURA.BAJA and tiempo == DATOS.TIEMPO.MUCHO):
        return DATOS.NIVEL_PIZZA.EN_SU_PUNTO
    if( temperatura == DATOS.TEMPERATURA.BAJA and tiempo == DATOS.TIEMPO.POCO):
        return DATOS.NIVEL_PIZZA.POCO_COCINADA
    if( temperatura == DATOS.TEMPERATURA.ALTA and tiempo == DATOS.TIEMPO.MUCHO):
        return DATOS.NIVEL_PIZZA.MUY_COCINADA
    if( temperatura == DATOS.TEMPERATURA.ALTA and tiempo == DATOS.TIEMPO.POCO):
        return DATOS.NIVEL_PIZZA.EN_SU_PUNTO
    
    #Return default?
    return DATOS.NIVEL_PIZZA.MUY_COCINADA

def func_ops(x, subconjunto, datos):
    """
    Calcula el valor de pertenencia de un valor x en un conjunto dado
    """
    temps = datos[subconjunto]
    mid = (temps[0] + temps[1]) / 2
    return (x - temps[0]) / (mid - temps[0]) if temps[0] <= x < mid else (temps[1] - x) / (temps[1] - mid) if mid <= x < temps[1] else 0

def reglas_temperatura(valor_temperatura):
    i_alta = DATOS.TEMPERATURA.ALTA
    i_baja = DATOS.TEMPERATURA.BAJA
    up_limit = DATOS.TEMPERATURA.VALORES[ i_alta ][-1]
    down_limit = DATOS.TEMPERATURA.VALORES[ i_baja ][0]
    if( valor_temperatura > up_limit or valor_temperatura < down_limit ):
        return 0
    else:
        pertenencia_baja = func_ops(valor_temperatura, DATOS.TEMPERATURA.BAJA, DATOS.TEMPERATURA.VALORES)
        pertenencia_alta = func_ops(valor_temperatura, DATOS.TEMPERATURA.ALTA, DATOS.TEMPERATURA.VALORES)
        print('Baja: ', pertenencia_baja)
        print('Alta: ', pertenencia_alta)
        return min(
            pertenencia_alta,
            pertenencia_baja
        )

def get_conjuntos(valor_temperatura, valores):
    conjuntos = []
    for key in valores:
        if valor_temperatura >= valores[key][0] and valor_temperatura <= valores[key][-1]:
            conjuntos.append(key)
    return conjuntos
    
def inferencia_fuzzyficar(valor_temperatura, valor_tiempo):
    conjuntos_temperatura = get_conjuntos( valor_temperatura, DATOS.TEMPERATURA.VALORES )
    conjuntos_tiempo = get_conjuntos( valor_tiempo, DATOS.TIEMPO.VALORES )
    for conj_temperatura in conjuntos_temperatura:
        for conj_tiempo in conjuntos_tiempo:
            pertenencia_temperatura = func_ops(valor_temperatura, conj_temperatura, DATOS.TEMPERATURA.VALORES)
            pertenencia_tiempo = func_ops(valor_tiempo, conj_tiempo, DATOS.TIEMPO.VALORES)
            pertenencia_pizza = min( pertenencia_temperatura, pertenencia_tiempo )
            conjunto_pizza = calcular_reglas(conj_temperatura, conj_tiempo)
            

 
# print(func_ops(180, DATOS.TEMPERATURA.BAJA, DATOS.TEMPERATURA.VALORES))
# print(func_ops(8.5, DATOS.TIEMPO.POCO, DATOS.TIEMPO.VALORES))
# print(func_ops(2, DATOS.NIVEL_PIZZA.POCO_COCINADA, DATOS.NIVEL_PIZZA.VALORES))

# print(calcular_reglas(DATOS.TEMPERATURA.ALTA, DATOS.TIEMPO.POCO))
# print(calcular_reglas(DATOS.TEMPERATURA.BAJA, DATOS.TIEMPO.MUCHO))

