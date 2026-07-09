#Diccionario base peliculas
peliculas = {
'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False]
}

#Diccionario base cartelera
cartelera = {
'P101': [5990, 40],
'P102': [7990, 0],
'P103': [4990, 25],
'P104': [6990, 12],
'P105': [8990, 8],
'P106': [7490, 3],
}

#Opciones validas de menu
ops=[1,2,3,4,5,6]

def validar_codigo(codigo):
    codigo_strip=codigo.strip()
    codigo_cap=codigo_strip.capitalize()
    if buscar_codigo(codigo_cap)==True:
        return False
    return True

def validar_titulo(titulo):
    titulo_strip=titulo.strip()
    if titulo_strip=="":
        print("Error: No hay datos")
        return False
    return True

def validar_gen(gen):
    gen_strip=gen.strip()
    if gen_strip=="":
        print("Error: No hay datos")
        return False
    return True

def validar_dur(dur):
    if dur<=0:
        print("Error: Duración debe ser mayor a cero")
        return False
    return True

def validar_clasif(clasif):
    if clasif.lower()=="a" or clasif.lower()=="b" or clasif.lower()=="c":
        return True
    return False

def validar_idioma(idioma):
    idioma_strip=idioma.strip()
    if idioma_strip=="":
        print("Error: No hay datos")
        return False
    return True

def validar_ddd(ddd):
    ddd_strip=ddd.strip()
    ddd_lower=ddd_strip.lower()
    if ddd_lower=="s" or ddd_lower=="n":
        return True
    return False

def validar_precio(precio):
    if precio<=0:
        print("Error: Precio debe ser mayor a cero")
        return False
    return True

def validar_cupos(cupos):
    if cupos<=0:
        print("Error: Precio debe ser mayor a cero")
        return False
    return True

def mostrar_menu():
        print("""=====MENÚ PRINCIPAL=====
    1. Cupos por género
    2. Búsqueda de películas por rango de precio
    3. Actualizar precio de película
    4. Agregar película
    5. Eliminar película
    6. Salir""")
    
def cupos_genero(genero):
    cupos=0
    gen_strip=genero.strip()
    gen_lower=gen_strip.lower()
    for i in range(len(peliculas)):
        iterable="P10"
        iterable_concat=iterable+str(i+1)
        if gen_lower==peliculas[iterable_concat][1]:
            cupos+=cartelera[iterable_concat][1]
        i+=1
    print(f"Cupos disponibles: {cupos}")

def buscar_pelicula(p_min, p_max):
    print("Peliculas disponibles en el rango: ")
    for i in range(len(cartelera)):
        iterable="P10"
        iterable_concat=iterable+str(i+1) 
        if cartelera[iterable_concat][0]>=p_min and cartelera[iterable_concat][0]<=p_max:
            print(peliculas[iterable_concat][0])

def buscar_codigo(codigo):
    for i in range(len(cartelera)):
        if codigo in cartelera:
            return True
    return False

def actualizar_precio(codigo,nuevo_precio):
    cartelera[codigo][0]=nuevo_precio
    print(f"Nuevo precio para {codigo}: {cartelera[codigo][0]}")

def agregar_pelicula(codigo,titulo,genero,duracion,clasif,idioma,ddd,precio,cupos):
    pelicula_nueva={codigo:[titulo,genero,duracion,clasif,idioma,ddd]}
    peliculas.append(pelicula_nueva)
    cartelera_nueva={codigo:[precio,cupos]}
    cartelera.append(cartelera_nueva)

def eliminar_pelicula(codigo):
    print("Error")

def leer_op(ops):
    try:
        op=int(input("Ingrese opción: "))
        if op in ops:
            return op
        else:
            print("Error: Opción no válida")
    except ValueError:
        print("Error: Opción no válida")

def main():
    while True:
        mostrar_menu()

        match leer_op(ops):
            case 1:
                gen=input("Ingrese género: ")
                cupos_genero(gen)
            case 2:
                try:
                    p_min=int(input("Ingrese precio mínimo: "))
                    p_max=int(input("Ingrese precio máximo: "))
                    if p_min<=0 or p_max<=0:
                        print("Error: Precio debe ser mayor a cero")
                    elif p_min>p_max:
                        print("Error: Precio mínimo no puede ser mayor al precio máximo.")
                    else:
                        buscar_pelicula(p_min,p_max)
                except ValueError:
                    print("Error: Precio debe ser un número entero")
            case 3:
                while True:
                    codigo=input("Ingrese código: ")
                    codigo=codigo.capitalize()
                    if buscar_codigo(codigo)==True:
                        try:
                            precio_nuevo=int(input("Ingrese nuevo precio: "))
                            actualizar_precio(codigo,precio_nuevo)
                            print("Precio actualizado")
                            otro_precio=input("¿Desea actualizar otro precio? s/n: ")
                            otro_precio_strip=otro_precio.strip()
                            if otro_precio_strip.lower=="s":
                                continue
                            else:
                                break
                        except ValueError:
                            print("Error: precio inválido")
                    else:
                        print("Codigo no existe")
            case 4:
                codigo=input("Ingrese codigo de nueva película: ")
                if validar_codigo(codigo)==False:
                    print("Codigo ya existe")
                    continue
                titulo=input("Ingrese titulo: ")
                if validar_titulo(titulo)==True:
                    genero=input("Ingrese género: ")
                    if validar_gen(genero)==True:
                        try:
                            duracion=int(input("Ingrese duración: "))
                        except ValueError:
                            print("Error: duración invalida")
                            continue
                        if validar_dur(duracion)==True:
                            clasif=input("Ingrese clasificación (A, B, C): ")
                            if validar_clasif(clasif)==True:
                                clasif=clasif.upper()
                                idioma=input("Ingrese idioma: ")
                                if validar_idioma(idioma)==True:
                                    status_3d=input("Es 3D? s/n: ")
                                    if validar_ddd(status_3d)==True:
                                        es_3d=True
                                    else:
                                        es_3d=False
                                    try:
                                        precio=int(input("Ingrese precio: "))
                                    except ValueError:
                                        print("Error: Precio no válido")
                                        continue
                                    if validar_precio(precio)==True:
                                        try:
                                            cupos=int(input("Ingrese cupos: "))
                                        except ValueError:
                                            print("Error: Cupos deben ser un número entero.")
                                        if validar_cupos(cupos)==True:
                                            agregar_pelicula(codigo,titulo,genero,duracion,clasif,idioma,es_3d,precio,cupos)
            case 5:
                codigo=input("Ingrese codigo: ")
                eliminar_pelicula(codigo)
            
            case 6:
                print("Programa finalizado.")
                break
                                                

main()