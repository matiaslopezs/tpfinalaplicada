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
    x: valor cuya pertenencia queremos calcular
    subconjunto: nombre del subconjunto. Ej.: DATOS.TIEMPO.POCO
    datos: valores del conjunto. Ej.: DATOS.TIEMPO.VALORES
    """
    temps = datos[subconjunto]
    mid = (temps[0] + temps[1]) / 2
    return (x - temps[0]) / (mid - temps[0]) if temps[0] <= x < mid else (temps[1] - x) / (temps[1] - mid) if mid <= x < temps[1] else 0

def func_ops_invert(pertenencia, subconjunto, datos):
    ## y = (x-a) / (mid-a)
    ## x = y (mid-a) + a
    temps = datos[subconjunto]
    mid = (temps[0] + temps[-1]) / 2
    invert_x = pertenencia * ( mid - temps[0] ) + temps[0]
    invert_x_2 = mid + ( mid - invert_x )
    return [invert_x, invert_x_2]


def get_conjuntos(valor, valores):
    """
    Retorna los conjuntos que participan para cierto valor
    """
    conjuntos = []
    for key in valores:
        if valor >= valores[key][0] and valor <= valores[key][-1]:
            conjuntos.append(key)
    return conjuntos
    
def fuzzyficar(valor_temperatura, valor_tiempo):
    #PRIMERO BUSCO QUE CONJUNTOS PARTICIPAN, SEGUN LOS VALORES INTRODUCIDOS
    conjuntos_temperatura = get_conjuntos( valor_temperatura, DATOS.TEMPERATURA.VALORES )
    conjuntos_tiempo = get_conjuntos( valor_tiempo, DATOS.TIEMPO.VALORES )
    nuevo_conjunto = []
    for conj_temperatura in conjuntos_temperatura:
        for conj_tiempo in conjuntos_tiempo:
            #RECORRO LOS CONJUNTOS PARA HALLAR LA REGLA QUE LES CORRESPONDE
            pertenencia_temperatura = func_ops(valor_temperatura, conj_temperatura, DATOS.TEMPERATURA.VALORES)
            pertenencia_tiempo = func_ops(valor_tiempo, conj_tiempo, DATOS.TIEMPO.VALORES)
            print("temperatura: ", pertenencia_temperatura)
            print("tiempo: ", pertenencia_tiempo)
            #HALLO EL valor DE PERTENENCIA DE LA TEMPERATURA, TIEMPO Y CON EL MIN EL DEL CONJUNTO DE pizza
            pertenencia_pizza = min( pertenencia_temperatura, pertenencia_tiempo )
            conjunto_pizza = calcular_reglas(conj_temperatura, conj_tiempo)
            #GUARDO RESULTADOS EN NUEVO CONJUNTO
            nuevo_conjunto.append({
                "conjunto": conjunto_pizza,
                "pertenencia": pertenencia_pizza,
            })
    return nuevo_conjunto

def defuzzyficar(conjunto):
    """
    Espera un vector del tipo : 
    [
        {"conjunto": conjunto_pizza, "pertenencia": 0.5},
        {"conjunto": conjunto_pizza, "pertenencia": 0.6}
    ]
    calcula el maximo punto del vector y saca el inverso de la funcion de pertenencia para ese valor
    """
    if len(conjunto) == 0:
        return 0
    obj_max = conjunto[0]
    for punto_inflex in conjunto:
        ##Recorro todos los puntos del conjunto
        if punto_inflex["pertenencia"] > obj_max["pertenencia"]:
            ##voy cargando el mayor en max_1
            obj_max = punto_inflex
    print("max", obj_max, "\n")
    y_vec = func_ops_invert(obj_max["pertenencia"], obj_max["conjunto"], DATOS.NIVEL_PIZZA.VALORES)
    print(y_vec)
    #retorno el promedio de los valores
    return sum( y_vec ) / float(len( y_vec ))

# print(func_ops(180, DATOS.TEMPERATURA.BAJA, DATOS.TEMPERATURA.VALORES))
# print(func_ops(8.5, DATOS.TIEMPO.POCO, DATOS.TIEMPO.VALORES))
# print(func_ops(2, DATOS.NIVEL_PIZZA.POCO_COCINADA, DATOS.NIVEL_PIZZA.VALORES))


conjunto = fuzzyficar( int(sys.argv[1]),  int(sys.argv[2]) )
print(conjunto)
y = defuzzyficar(conjunto)
print(y)
