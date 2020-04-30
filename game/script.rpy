# DECLARAMOS LOS PERSONAJES
define m = Character("Miquel", color = "#37dc1d")
define tu = Character("John", color = "#ffff33")


# FUNCION DONDE COMIENZA EL JUEGO
label start:

    # CARGAMOS EL FONDO
    scene habitacion with fade

    #CARGAMOS Y REPRODUCIMOS LA MUSICA DE FONDO
    play music "audio/musica.mp3" loop fadein 1.0


    #MOSTRAMOS POR PANTALLA EL PERSONAJE Y LO CENTRAMOS
    show miquel at center:
         # REDUCIMOS EL TAMAÑO

    #COMIENZA A MOSTRAR TEXTOS
    m"Buenas, creo que me acuerdo de ti. Tú eras el de Telegram, ¿verdad?"



    #MOSTRAMOS POR PANTALLA LA OPCION
    menu:
        "Si.":
            jump si
        "No.":
            jump no

# ESCENA 2 DEL TUTORIAL
label si:

    # CARGAMOS EL FONDO CON UNA TRANSICION
    scene habitacion with fade
    show miquel at center

    m"¿Te acuerdas del videojuego que estaba haciendo?"

    # SALTAMOS A LA NUEVA ESCENA
    menu:
        "Si, que me dijiste que si quería participar":
            jump si2
        "No, ¿qué juego?":
            jump no2
label no:
    scene habitacion with fade

    show miquel at center
    m"Pues no se qué haces aquí."

# ESCENA DONDE HABLAN LOS PERSONAJES
label no2:
    scene habitacion
    show miquel at center

    m"Eres un mentiroso, si sabes de lo que hablo..."
jump si
label si2:

    scene habitacion

    show miquel at center:


    m"¡Pues ya está casi acabado!"

    show miquel at center

    m"He estado trabajando mucho en él y me está quedando bastante chulo, la verdad... ¿quieres probarlo?"
    # MOSTRAMOS LAS DOS OPCIONES
    menu:
        "Venga, enséñamelo.":
            jump ver
        "Qué va, no me interesa":
            jump negarse

# ESCENA EN LA QUE DECIMOS LA VERDAD
label ver:
    scene habitacion
    show miquel at center:

    m"¡Mira cómo mola!"
    menu:
        "Ver el juego":
            jump imagen1


# ESCENA EN LA QUE MENTIMOS
label negarse:

    m"No digas tonterías, te va a encantar, mira."
    jump imagen1


label imagen1:
    scene minecraft1 with fade
    m"Este es el escenario principal"
    jump imagen2
label imagen2:
    scene minecraft2 with fade
    m"Este es el personaje que he creado"
    jump imagen3
label imagen3:
    scene minecraft3 with fade
    m"Y este es uno de los ambientes"
    jump dialogo2

label dialogo2:
    scene habitacion with fade
    show miquel at center
    m"¿Te ha gustado?"
    menu:
        "Sí, está muy bien.":
            jump si3

        "La verdad es que no me ha gustado nada.":
            jump no3

label si3:
    scene habitacion
    show miquel at center
    m"Muchas gracias, tu respuesta me hace muy feliz y me anima a seguir con este trabajo y terminar el juego."
    jump salto
label no3:
    scene habitacion
    show miquel at center
    m"¡Qué desagradable eres!"
    jump salto
label salto:
    scene fondonegro
    "SEIS MESES MAS TARDE..."
    jump final
label final:
    scene parque with fade
    show miquel at center
    m"¡Hola!, venía a decirte que ya he terminado mi videojuego y que está a la venta."
    menu:
        "¿Qué tal ha ido?":
            jump quetal

label quetal:
    scene parque
    show miquel at center
    m"Ha salido muy bien. Se ha vendido bien y poco a poco van aumentando las ventas."
    menu:
        "Me alegro mucho Miquel.":
            jump mealegro

        "Te lo mereces, pero la verdad es que no me gustó nada el juego.":
            jump finalmalo

label mealegro:
    scene parque
    show miquel at center
    m"Muchas gracias. Gracias a ti y a tu apoyo conseguí sacarlo adelante."
    menu:
        "De nada Miquel, ¿cómo te va en el instituto?":
            jump instituto

label instituto:
    scene parque
    show miquel at center
    m"Pues gracias a todo esto me he vuelto muy popular y ya tengo más amigos, pero tu siempre serás mi primer amigo y por eso te he metido en los créditos del videojuego para que estés siempre presente."
    menu:
        "Muchas gracias amigo, espero que todo te vaya bien.":
            jump finalisimo

label finalisimo:
    scene parque with fade
    show miquel at center
    m"Muchas gracias amigo, ya hablaremos si me surge algún otro proyecto. Gracias por todo."
    jump fin
label finalmalo:
    scene parque with fade
    show miquel at center
    m"Muchas gracias por nada, me da igual tu opinión, no necesito tu penosa aprobación para mi videojuego, creía que eramos amigos..."
    jump fin








label fin:

    # TERMINA EL JUEGO

    return
