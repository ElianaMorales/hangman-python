import random
import sys


def crearDiccPalabrasReemplazar(default="ZZZZZZZZ"):
    """Devuelve un diccionario donde las claves son las palabras a reemplazar y el valor
    palabra reemplazante"""
    dicc_reemplazar = {}
    dicc_reemplazar[","] = ""
    linea = leer(reemplazar)
    while linea != default:
        caracteres = linea.rstrip().split(",")
        dicc_reemplazar[caracteres[0]] = caracteres[1]
        linea = leer(reemplazar)
    return dicc_reemplazar


def leer(archivo, default="ZZZZZZZZ"):
    """"Recibe un archivo y devuelve la linea en mayuscula si no es fin de archivo, sino devuelve default"""
    """"PreCondicion: Archivo abierto en modo lectura(r)"""
    linea = archivo.readline()
    if linea != "":
        return linea.upper()
    else:
        return default


def validarPalabra(palabra, dicc_reemplazar):
    """Recibe una palabra y un diccionario con palabras/caracteres a reemplazar ; y devuelve una palabra validada
    (palabra la cual sus caracteres fueron reemplazados o no se encuentran en el archivo reemplazar.csv)"""
    for palabra_reemplazar in dicc_reemplazar.keys():
        if palabra_reemplazar in palabra:
            palabravalida = palabra.replace(palabra_reemplazar, dicc_reemplazar[palabra_reemplazar])
            palabra = palabravalida
    return palabra


def listaPalabrasValidas(dicc_reemplazar, archivo, archivoEscribir, default="ZZZZZZZZ"):
    """Recibe un diccionario con palabras/caracteres a reemplazar ,un archivo y un archivo a escribir ; crea un
    diccionario con palabras validas"""
    """PreCondicion: Archivo abierto en modo lectura (r) """
    dicc_palabrasValidas = {}
    linea = leer(archivo)
    while linea != default:
        palabras = linea.rstrip().split()
        for i in range(len(palabras)):
            palabravalida = validarPalabra(palabras[i], dicc_reemplazar)
            if palabravalida not in dicc_palabrasValidas and len(palabravalida) > 0:
                dicc_palabrasValidas[palabravalida] = 1
        linea = leer(archivo)
    escribirArchivo(archivoEscribir, list(dicc_palabrasValidas.keys()))


def escribirArchivo(archivo, lista):
    """"Recibe un archivo y una lista ; escribe sobre el archivo cada elemento de la lista en forma
    ordenada separandolos por renglones. Vuelve el puntero del archivo al inicio"""
    for palabra in sorted(lista):
        archivo.write(palabra + "\n")
    archivo.seek(0)


def merge(archivo1, archivo2, archivo3, palabras_Validas_Textos, default="ZZZZZZZZ"):
    """Recibe 4 archivos, mientras alguno de los 3 archivos no halla llegado a su fin ,escribe en un archivo el conjunto
    de palabras de estos archivos en orden y sin repetir. Cuenta el total de palabras y la cantidad de palabras por
    longitud de letras y los imprime por pantalla"""
    """PreCondicion: 3 archivos abiertos en modo lectura y escritura (r+) y 1 archivo abierto en modo escritura(w)"""
    palabra1 = leer(archivo1).rstrip()
    palabra2 = leer(archivo2).rstrip()
    palabra3 = leer(archivo3).rstrip()
    total_palabras = 0
    dicc_longitud = {}
    dicc_palabras = {}
    while palabra1 != default or palabra2 != default or palabra3 != default:
        menor = min(palabra1, palabra2, palabra3)
        while palabra1 == menor:
            if palabra1 not in dicc_palabras:
                palabras_Validas_Textos.write(palabra1 + "\n")
                dicc_palabras[palabra1] = 1
            else:
                dicc_palabras[palabra1] += 1
            if len(palabra1) not in dicc_longitud:
                dicc_longitud[len(palabra1)] = 1
            else:
                dicc_longitud[len(palabra1)] += 1
            total_palabras += 1
            palabra1 = leer(archivo1).rstrip()
        while palabra2 == menor:
            if palabra2 not in dicc_palabras:
                palabras_Validas_Textos.write(palabra2 + "\n")
                dicc_palabras[palabra2] = 1
            else:
                dicc_palabras[palabra2] += 1
            if len(palabra2) not in dicc_longitud:
                dicc_longitud[len(palabra2)] = 1
            else:
                dicc_longitud[len(palabra2)] += 1
            total_palabras += 1
            palabra2 = leer(archivo2).rstrip()
        while palabra3 == menor:
            if palabra3 not in dicc_palabras:
                palabras_Validas_Textos.write(palabra3 + "\n")
                dicc_palabras[palabra3] = 1
            else:
                dicc_palabras[palabra3] += 1
            if len(palabra3) not in dicc_longitud:
                dicc_longitud[len(palabra3)] = 1
            else:
                dicc_longitud[len(palabra3)] += 1
            total_palabras += 1
            palabra3 = leer(archivo3).rstrip()
    print("Letras por palabra,Cantidad total: {}".format(sorted(list(dicc_longitud.items()))))
    print("Cantidad total de palabras: {}".format(total_palabras))
    return dicc_palabras


def leer_constantes():
    """Se lee un archivo en donde cada linea tiene el nombre y valor de las constantes. Se imprime cada linea y los
    valores se guardan en una lista. Se devuelve cada elemento de la lista para luego asignarlas como constantes del
    programa."""
    nombres_constantes = ['L', 'M', 'N', 'X', 'Y', 'Z']
    l_constantes = []
    i = 0
    constantes = open('Configuracion.txt')
    for linea in constantes:
        nombre, valor = linea.rstrip().split(' ')
        print('{0} = {1} ({2})'.format(nombres_constantes[i], valor, nombre))
        l_constantes.append(int(valor))
        i += 1
    return l_constantes[0], l_constantes[1], l_constantes[2], l_constantes[3], l_constantes[4], l_constantes[5]
        

def cantidad_de_jugadores():
    """Solicita el ingreso de la cantidad de jugadores, validando que sean números enteros entre 1(uno) y N."""
    cantidad = input('\nIngrese la cantidad de jugadores que son(no mayor a {}): '.format(N))
    while (cantidad.isdigit() is False) or (int(cantidad) < 0) or (int(cantidad) > N) or (cantidad == ''):
        print('Error! Debe ingresar un número entero entre 1 y {}. Inténtelo nuevamente!'.format(N))
        cantidad = input('Ingrese la cantidad de jugadores que son(no mayor a {})): '.format(N))
    return int(cantidad)


def ingreso_nombres(cantidad):
    """Se solicita el ingreso de los nombres de cada jugador, según la cantidad de jugadores ya previamente ingresado,
    los cuales se validan que sean letras con o sin espacios en blanco y que no se repita el nombre del jugador, y se
    almacenan todos como claves de un diccionario."""
    datos_inicio = {}
    jugadores = []
    for i in range(1, cantidad+1):
        jugador = input('Ingrese el nombre del {}° jugador: '.format(i))
        while ((jugador.replace(' ', '')).isalpha() is False) or (jugador.upper() in jugadores):
            print('Error! Debe tener solo letras, con o sin espacios y sin repetir nombres. Inténtelo nuevamente!')
            jugador = input('Ingrese el nombre del {}° jugador: '.format(i))
        jugador = jugador.upper()
        datos_inicio[jugador] = {'palabra': '', 'puntos': 0, 'aciertos': 0, 'desaciertos': 0, 'estado': 'PERDEDOR',
                                 'intentos': 7}
        jugadores.append(jugador)
        print('Bienvenido/a jugador/a ', jugador)
    return datos_inicio


def imprimir_orden_de_juego(datos_inicio):
    """Se recibe un diccionario previamente cargado en donde sus claves son los nombres de los jugadores y devuelve e
    imprime una lista con el orden de juego para cada jugador de manera aleatoria."""
    jugadores = list(datos_inicio.keys())
    random.shuffle(jugadores)
    print('El orden de juego es: ')
    for (posicion, item) in enumerate(jugadores):
        print('{}°:{}'.format(posicion+1, item))
    return jugadores


def ingresar_longitud():
    """Solicita el ingreso de la cantidad de letras de una palabra y valida que sea un número entero y mayor o igual a"""
    longitud = input('Ingresen la cantidad de letras de las palabras que intentarán adivinar: ')
    while (longitud.isdigit() is False) or (int(longitud) < L) or (cantidad == ''):
        print('Error! Debe ingresar un número entero mayor o igual a {}. Inténtelo Nuevamente!'.format(L))
        longitud = input('Ingresen la cantidad de letras de las palabras que intentarán adivinar: ')
    return int(longitud)


def lista_palabras_seleccionadas(dicc_libreria):
    """Se recibe un diccionario en el cual sus claves son una lista de palabras sin repetir. Selecciona palabras que
    tengan la cantidad de letras que devuelve una función a la que se llama y las ingresa en una lista. Si la lista
    queda vacía, se vuelve a llamar a la funcion para que se ingrese otra cantidad de letras. Se devuelve la lista con
    las palabras seleccionadas."""
    libreria = dicc_libreria.keys()
    lista_palabras = []
    total = 0
    while total == 0:
        longitud = ingresar_longitud()
        for palabra in libreria:
            if len(palabra) == longitud:
                lista_palabras.append(palabra)
        total = len(lista_palabras)
        if total == 0:
            print('Oops! No hay palabras con esa cantidad de letras. Inténtalo nuevamente!')
    return lista_palabras


def asignar_palabra(datos_inicio, dicc_libreria):
    """De una lista de palabras seleccionadas que se obtiene de una funcion, las cuales poseen igual cantidad de
    caracteres, se selecciona una palabra aleatoria para cada jugador."""
    lista_palabras = lista_palabras_seleccionadas(dicc_libreria)
    for jugador in datos_inicio:
        datos_inicio[jugador]['palabra'] = random.choice(lista_palabras)
    return datos_inicio


def menu():
    """"Mensaje de inicio del juego con las instrucciones,luego muestra el diccionario con las palabras a jugar.
    Autores: Manuel Marcos, Sabrina L. Jodara, Eliana Morales.
    """
    textoMenu = """
    ==================================================¡BIENVENIDO!======================================================

    Vamos a jugar al AHORCADO MULTIJUGADOR. Las reglas son:

    * Se puede juegar hasta {} jugadores
    * Al principio del juego se ingresará la cantidad de letras de las palabras que intentarán adivinar no mayor a {}.
    * A cada jugador se le asignará una palabra aleatoria para adivinar con esa cantidad de letras
    * Por cada acierto a ese jugador se le sumará {} puntos y por cada desacierto se restarán {} puntos. Aunque acierte
    o desacierte, seguirá el turno del jugador siguiente
    * Cada jugador tiene hasta {} desaciertos. Cuando llegue a ese momento, ese jugador pierde. Mientras, el resto puede 
    seguir jugando hasta que uno gane o todos pierdan.
    * El primero que acierta toda las letras ¡GANA!
    """
    print(textoMenu.format(N, L, X, Y, M))
    arranque = (input('¿Empezamos? (S/N): ')).upper()
    while arranque != 'S':
        if arranque == 'N':
            sys.exit('¡HASTA LA PRÓXIMA!')
        else:
            print('Error! Ingresar "S" para empezar o "N" para salir')
            arranque = (input('¿Empezamos? (S/N): ')).upper()
    print('¡QUE COMIENCE EL JUEGO! BUENA SUERTE')


def crear_interfaz(datos_inicio, jugador):
    """Este modulo se encarga de crear una interfaz que muestre al usuario guiones en el lugar que van las letras de la
    palabra asignada.
    """
    letras_que_faltan = []
    palabra = datos_inicio[jugador]['palabra']
    for caracter in palabra:
        letras_que_faltan.append(' _ ')
    return letras_que_faltan


def asignar_interfaz(datos_inicio, mostrar_usuario):
    """Este modulo le asigna una interfaz a cada jugador con los espacios correspondientes de cada palabra.
    """
    for jugador in datos_inicio:
        mostrar_usuario[jugador] = crear_interfaz(datos_inicio, jugador)
    return mostrar_usuario


def cambiar_letras_que_faltan(indice, letra, mostrar_usuario, jugador):
    """Reemplaza los guiones por la letra que va en ese lugar cuando un jugador adivina.
    """
    mostrar_usuario[jugador].insert(indice, letra)
    del mostrar_usuario[jugador][indice+1]
    return mostrar_usuario[jugador]


def mostrar_letras_que_faltan(mostrar_usuario, jugador):
    c = ''
    for caracter in mostrar_usuario[jugador]:
        c = c+' '.join(caracter)
    return c


def ahorcado(datos_inicio, jugador):
    """Muestra el dibujo del ahorcado. Autora: Eliana Morales."""
    ahorcadoDibujo = ['''
      +---+
          |
          |
          |
          |
          |
    =========\n\n''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========\n\n''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========\n\n''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========\n\n''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========\n\n''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========\n\n''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========\n\n''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ¡¡¡AHORCADO!!!\n\n''']
    c = datos_inicio[jugador]['desaciertos']
    print(ahorcadoDibujo[c])
    return


def asegurar_letra(letra):
    """Verfica si la letra ingresada por el usuario es única, y un caracter alfabético sin espacios
    en caso de que no cumpla con esto se pide que vuelva a ingresar."""
    while (letra.isalpha() is False or (letra == ' ')) and len(letra) == 1:
        print('Error. Sólo puede ingresar un carácter alfabético y sin espacios')
        letra = input('Ingrese una letra: ')
        letra = letra.upper()
    return letra


def letra_repetida(letra, mostrar_usuario, jugador):
    """comprueba si el usuario ya ingreso una letra."""
    while letra in mostrar_usuario[jugador]:
        print('Ya ha ingresado esa letra, intente otra: ')
        letra = input('Ingrese una letra: ')
        letra.upper()
    return letra


def si_hay_letra(datos_inicio, jugador, palabra, letra, mostrar_usuario):
    """Este modulo se encarga de verificar si la letra ingresada por el usuario se encuentra en la
    palabra asignada, muestra su posición, le suma un punto y un acierto."""
    indice = 0
    while indice < len(palabra):
        if palabra[indice] == letra:
            print('¡Correcto! Te quedan {} intentos'.format(datos_inicio[jugador]['intentos']))
            print('La letra "{}" se encuentra en la posición {}'.format(letra, indice+1))
            datos_inicio[jugador]['puntos'] += X
            datos_inicio[jugador]['aciertos'] += 1
            mostrar_usuario[jugador] = cambiar_letras_que_faltan(indice, letra, mostrar_usuario, jugador)
            print(mostrar_letras_que_faltan(mostrar_usuario, jugador))
        indice += 1
    return datos_inicio[jugador]


def si_no_hay_letra(datos_inicio, jugador, letra):
    """Muestra un mensaje por pantalla informando al usuario que la letra ingresada 
    no se encuentra en la palabra, le resta dos puntos y suma un desacierto.
    """
    datos_inicio[jugador]['desaciertos'] += 1
    datos_inicio[jugador]['puntos'] -= Y
    print('¡Ups! La letra {} no está en la palabra'.format(letra))
    return datos_inicio[jugador]


def mostrar_ganadores(datos_inicio, jugador):
    """Verifica si hay ganadores o perdedores e imprime un mensaje informando a los jugadores
    en caso de que los haya.
    """
    if datos_inicio[jugador]['estado'] == 'GANADOR':
        print('¡Felicitaciones! {} ha adivinado la palabra: {}'.format(jugador, datos_inicio[jugador]['palabra']))
    if datos_inicio[jugador]['desaciertos'] == 7:
        print('¡{} ha perdido! La palabra era: {}'.format(jugador, datos_inicio[jugador]['palabra']))
    return


def comprobar_ganadores(datos_inicio, jugador):
    """Este modulo verifica si la cant. de letras en la palabra es igual a la de aciertos
    en ese caso cambia el estado del jugador a GANADOR."""
    if len(datos_inicio[jugador]['palabra']) == datos_inicio[jugador]['aciertos']:
        datos_inicio[jugador]['estado'] = 'GANADOR'
    return datos_inicio[jugador]['estado']


def mostrar_puntaje(datos_inicio, jugador):
    """Muestra un mensaje en pantalla con los datos de cada jugador."""
    print('Aciertos: {} '.format(datos_inicio[jugador]['aciertos']))
    print('Desaciertos: {}'.format(datos_inicio[jugador]['desaciertos']))
    print('Puntaje: {}'.format(datos_inicio[jugador]['puntos']))
    return


def inicio_turno(jugador, mostrar_usuario):
    """Primera parte del turno. Se pide el ingreso de una letra y se hacen las comprobaciones."""
    print('JUEGA AHORA: ', jugador)
    print('PALABRA: ', mostrar_letras_que_faltan(mostrar_usuario, jugador))
    letra = input('Ingrese una letra: ')
    letra = letra.upper()
    letra = asegurar_letra(letra)
    return letra


def eliminar_perdedor_ronda(lista_inicio_por_jugador, datos_nuevos):
    """Revisa si hay perdedores una vez terminada la ronda y los saca del juego."""
    for tupla in lista_inicio_por_jugador:
        jugador = tupla[0]
        if tupla[1]['desaciertos'] < 7 and tupla[1]['intentos'] >= -1:
            datos_nuevos[jugador] = tupla[1]
    return datos_nuevos


def si_no_hay_ganador(lista_resultados):
    perdedores = 0
    for i in range(len(lista_resultados)):
        for lista in lista_resultados:
            if lista[i]['estado'] == 'PERDEDOR':
                perdedores += 1
    if perdedores == len(lista_resultados):
        w = '¡LA CASA GANA! MEJOR SUERTE PARA LA PRÓXIMA :D'
        print(w)
    return


def resultado_fin_partida(lista_resultados, datos_final):
    if len(lista_resultados) > 0:
        si_no_hay_ganador(lista_resultados)
    for jugador in datos_final:
        print('*** JUGADOR: {}'.format(jugador))                    
        mostrar_puntaje(datos_final, jugador)
    return


def turno_por_jugador(datos_inicio, jugador, mostrar_usuario):
    """Le da un turno a cada jugador."""
    letras_equivocadas = []
    letra = inicio_turno(jugador, mostrar_usuario)
    letra = asegurar_letra(letra)
    palabra = datos_inicio[jugador]['palabra']
    if (letra in palabra) and (datos_inicio[jugador]['intentos'] > -1):
        if (letra in mostrar_usuario[jugador]) or (letra in letras_equivocadas):
            letra = letra_repetida(letra, mostrar_usuario, jugador)
        else:
            datos_inicio[jugador] = si_hay_letra(datos_inicio, jugador, palabra, letra, mostrar_usuario)
        datos_inicio[jugador]['estado'] = comprobar_ganadores(datos_inicio, jugador)
    elif letra not in palabra:
        letras_equivocadas.append(letra)
        datos_inicio[jugador] = si_no_hay_letra(datos_inicio, jugador, letra)
        print('¡Has fallado! :( te quedan {} intentos'.format(datos_inicio[jugador]['intentos']))
        datos_inicio[jugador]['estado'] = comprobar_ganadores(datos_inicio, jugador)
        datos_inicio[jugador]['intentos'] = datos_inicio[jugador]['intentos']-1
    mostrar_puntaje(datos_inicio, jugador)
    ahorcado(datos_inicio, jugador)
    datos_inicio[jugador]['estado'] = comprobar_ganadores(datos_inicio, jugador)
    return datos_inicio[jugador]


def ronda_jugadores(datos_inicio, mostrar_usuario, datos_nuevo, jugadores_ordenados):
    """Realiza una ronda de juego con un turno por jugador."""
    for jugador in jugadores_ordenados:
        if (datos_inicio[jugador]['intentos'] >= -1 and datos_inicio[jugador]['desaciertos'] <= 7) and \
                datos_inicio[jugador]['estado'] == 'PERDEDOR':
            datos_inicio[jugador] = turno_por_jugador(datos_inicio, jugador, mostrar_usuario)
            datos_inicio[jugador]['estado'] = comprobar_ganadores(datos_inicio, jugador)
            if datos_inicio[jugador]['estado'] == 'GANADOR':
                break
        mostrar_ganadores(datos_inicio, jugador)
        lista_menu = list(datos_inicio.items())
        datos_inicio = eliminar_perdedor_ronda(lista_menu, datos_nuevo)
    return datos_inicio


def partida(datos_inicio, mostrar_usuario, datos_nuevo, jugadores_ordenados):
    """Repite las rondas hasta que encuentre un ganador o todos pierdan."""
    datos_final = {}
    boolean = True
    lista_resultados = []
    while boolean:
        datos_inicio = ronda_jugadores(datos_inicio, mostrar_usuario, datos_nuevo, jugadores_ordenados)
        for jugador in datos_inicio:
            datos_final[jugador] = datos_inicio[jugador]
        for jugador in datos_inicio:
            if len(datos_inicio[jugador]['palabra']) == datos_inicio[jugador]['aciertos']:
                mostrar_ganadores(datos_inicio, jugador)
                datos_inicio[jugador]['puntos'] += Z
                boolean = False
                break
            elif datos_inicio[jugador]['estado'] == 'GANADOR':
                mostrar_ganadores(datos_inicio, jugador)
                lista_resultados.append(list(datos_inicio.values()))
                print(lista_resultados)
                datos_inicio[jugador]['puntos'] += Z
                boolean = False
                break
            elif datos_inicio[jugador]['desaciertos'] == 7:
                lista_resultados.append(list(datos_inicio.values()))
                print(lista_resultados)
                boolean = False
                break
            else:
                boolean = True
    resultado_fin_partida(lista_resultados, datos_final)
    return datos_inicio


def reiniciar_partida(datos_inicio, mostrar_usuario, datos_nuevo, dicc_libreria, jugadores_ordenados):
    """Reinicia la partida en caso de que los usuarios quieran."""
    final_archivo = {}
    for jugador in datos_inicio:
        final_archivo[jugador] = datos_inicio[jugador]
    tupla_nuevo_inicio = []
    strings = {}
    opcion = validar_reiniciar_partida()
    if opcion == 'N':
        generar_archivo_juego(final_archivo, jugadores_ordenados)
    while opcion == 'S':
        for jugador in datos_inicio:
            string = final_archivo[jugador]['palabra']
            strings[jugador] = string
            datos_inicio[jugador]['palabra'] = ''
            datos_inicio[jugador]['aciertos'] = 0
            datos_inicio[jugador]['desaciertos'] = 0
            datos_inicio[jugador]['estado'] = 'PERDEDOR'
            datos_inicio[jugador]['intentos'] = 7
            final_archivo_tuplas = list(final_archivo[jugador].items())
            tupla_nuevo_inicio.append((jugador, final_archivo_tuplas[1][1]))
        print('\n¡Entonces jugaremos nuevamente! Ahora el orden de juego sera por mayor puntaje. BUENA SUERTE!!\n')
        jugadores_ordenados = ordenar_jugadores_por_puntos(tupla_nuevo_inicio)
        datos_inicio = asignar_palabra(datos_inicio, dicc_libreria)
        mostrar_usuario = asignar_interfaz(datos_inicio, mostrar_usuario)
        datos_inicio = partida(datos_inicio, mostrar_usuario, datos_nuevo, jugadores_ordenados)
        for jugador in datos_inicio:
            strings[jugador] += ' ' + datos_inicio[jugador]['palabra']
            final_archivo[jugador]['palabra'] = strings[jugador]
            final_archivo[jugador]['puntos'] += datos_inicio[jugador]['puntos']
            final_archivo[jugador]['aciertos'] += datos_inicio[jugador]['aciertos']
            final_archivo[jugador]['desaciertos'] += datos_inicio[jugador]['desaciertos']
        print(final_archivo)
        opcion = validar_reiniciar_partida()
    generar_archivo_juego(final_archivo, jugadores_ordenados)


def validar_reiniciar_partida():
    """Solicita el ingreso de 'S' para seguir jugando o 'N' para salir. Valida el ingreso y sino devuelve un mensaje de
    error."""
    opcion = (input('¿Desea jugar otra partida? (S/N):  ')).upper()
    while opcion != 'S' and opcion != 'N':
        print('Error! Ingresar "S" para seguir jugando o "N" para salir')
        opcion = (input('¿Desea jugar otra partida? (S/N):  ')).upper()
    return opcion


def ordenar_jugadores_por_puntos(tupla_nuevo_inicio):
    """Se genera una lista de los jugadores ordenados de mayor a menor puntaje. Autora: Sabrina L. Jodara"""
    jugadores_ordenados = []
    tupla_nuevo_inicio.sort()
    nuevo_inicio_ordenado = sorted(tupla_nuevo_inicio, key=lambda tup: tup[1], reverse=True)
    n = len(nuevo_inicio_ordenado)
    for i in range(n):
            jugadores_ordenados.append(nuevo_inicio_ordenado[i][0])
    return jugadores_ordenados


def generar_archivo_juego(datos, jugadores_ordenados):
    """Se genera archivo para guardar información final del juego de todos los jugadores. Luego se imprime por pantalla.
    """
    lista_linea = []
    partida = open('Partida.csv', 'w+')
    for jugador in jugadores_ordenados:
        lista_linea = [jugador, str(datos[jugador]['aciertos']), str(datos[jugador]['desaciertos']),
                       str(datos[jugador]['puntos']), datos[jugador]['palabra']+'\n']
        line = ','.join(lista_linea)
        partida.write(line)
    print('Los resultados finales por jugador son:')
    partida.seek(0)
    for linea in partida:
        jug, ac, des, pts, pal = linea.rstrip(' \n').split(',')
        print('**{0}= ACIERTOS:{1}  DESACIERTOS: {2}  PUNTAJE TOTAL: {3}  PALABRAS: {4}'.format(jug, ac, des, pts, pal))
    print('Hasta la próxima!')
    partida.close()
    return


# Bloque que abre los archivos #
lasMilYUnaNoches = open("Las 1000 Noches y 1 Noche.txt", "r+")
laAranaNegra = open("La araña negra - tomo 1.txt", "r+")
cuentos = open("Cuentos.txt", "r+")
reemplazar = open("Reemplazar.csv", "r+")
palabras_LasMilYUnaNoches = open("Palabras Las Mil y Una Noches.txt", "w+")
palabras_LaAranaNegra = open("Palabras La arana Negra.txt", "w+")
palabras_Cuentos = open("Palabras Cuentos.txt", "w+")
palabras_Validas_Textos = open("Palabras.txt", "w")

# Bloque que crea el dicc con las palabras a reemplazar #
dicc_reemplazar = crearDiccPalabrasReemplazar()

# Bloque que lee los archivos y depura las palabra #
"""Las Mil y Una Noches"""
listaPalabrasValidas(dicc_reemplazar, lasMilYUnaNoches, palabras_LasMilYUnaNoches)
lasMilYUnaNoches.close()
""""La Arana Negra"""
listaPalabrasValidas(dicc_reemplazar, laAranaNegra, palabras_LaAranaNegra)
laAranaNegra.close()
""""Cuentos"""
listaPalabrasValidas(dicc_reemplazar, cuentos, palabras_Cuentos)
cuentos.close()

# Merge #
dicc_libreria = merge(palabras_LasMilYUnaNoches, palabras_LaAranaNegra, palabras_Cuentos, palabras_Validas_Textos)
palabras_LasMilYUnaNoches.close()
palabras_LaAranaNegra.close()
palabras_Cuentos.close()
palabras_Validas_Textos.close()

# BLOQUE PRINCIPAL #
L, M, N, X, Y, Z = leer_constantes()
menu()
cantidad = cantidad_de_jugadores()
datos_inicio = ingreso_nombres(cantidad)
jugadores_ordenados = imprimir_orden_de_juego(datos_inicio)
mostrar_usuario = {}
datos_nuevo = {}
datos_inicio = asignar_palabra(datos_inicio, dicc_libreria)
mostrar_usuario = asignar_interfaz(datos_inicio, mostrar_usuario)
datos_inicio = partida(datos_inicio, mostrar_usuario, datos_nuevo, jugadores_ordenados)
reiniciar_partida(datos_inicio, mostrar_usuario, datos_nuevo, dicc_libreria, jugadores_ordenados)

