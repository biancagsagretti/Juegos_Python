

from logging.handlers import WatchedFileHandler


listado = [
    {
        "pregunta": "Translate: He is a football player",
        "opciones": [
            "El es un jugador de futbol",
            "Ella es una jugadora de tennis",
            "A el le gusta tocar la guitarra"
        ],
        "respuesta":1
    },
    {
        "pregunta": "Traducir: Cuantos años tenes?",
        "opciones": [
            "What time is it?",
            "Do you like pizza?",
            "How old are you?"
        ],
        "respuesta":3
    },  
      {
        "pregunta": "Traducir: Qué hora es?",
        "opciones": [
            "What time is it?",
            "Do you like pizza?",
            "How old are you?"
        ],
        "respuesta":1
    },  
    {
        "pregunta": "Translate: He works in an office",
        "opciones": [
            "Él es un jugador de futbol",
            "Él trabaja en una oficina",
            "Él tiene un perro"
        ],
        "respuesta":2
    }
]

print("Let's play!\n")

indice = 1
for entrada in listado:
    
    print("Pregunta {}: \n".format(indice))
    print(entrada["pregunta"])
    indice +=1
    print("Opciones: ")

    indice_opciones = 1
    for opcion in entrada["opciones"]:
        print("{}: {}".format(indice_opciones, opcion))
        indice_opciones += 1

    print("0: Salir del juego")
    respuesta = int(input("> "))
    
    if respuesta == 0:
       print("Estás seguro? y/n.")
       respuesta = input(">")
       if respuesta.lower()=="y":
            break
   
    
#     # Agregar la validacion para comprobar si el numero ingresado por el usuario
#     # Coincide con entrada["respuesta"]
    
    indice_respuesta =1
    
    if respuesta == entrada["respuesta"]:
        print("La respuesta es correcta")
        indice_respuesta +=1
    else:
        print("La respuesta es incorrecta")
        print("La respuesta correcta es:", entrada["respuesta"])
            


      
print("Hasta pronto!")



