import random

def obtener_palabra_aleatoria():
    palabras = ["computadora", "teclado", "ratón", "monitor", "ventana", "puerta",
                "libro", "papel", "lapicera", "pluma", "lápiz", "silla", "mesa",
                "cama", "almohada", "televisor", "radio", "teléfono", "celular",
                "cable", "internet", "web", "página", "palabra", "frase", "texto",
                "imagen", "foto", "video", "música", "sonido", "audio", "botón",
                "ventilador", "aire", "agua", "tierra", "fuego", "aire acondicionado",
                "calor", "frío", "color", "rojo", "verde", "azul", "amarillo",
                "naranja", "negro", "blanco", "gris", "morado", "rosa", "mariposa",
                "libélula", "araña", "escarabajo", "cielo", "nube", "sol", "luna",
                "estrella", "galaxia", "universo", "planeta", "tierra", "satélite",
                "astronauta", "nave", "ovni", "extraterrestre", "cara", "ojos",
                "nariz", "boca", "orejas", "cabello", "barba", "bigote", "labios",
                "dientes", "lengua", "dedo", "mano", "brazo", "pierna", "pie",
                "dedo del pie", "uña", "corazón", "amor", "sentimiento", "emoción",
                "familia", "madre", "padre", "hermano", "hermana", "abuelo", "abuela",
                "tío", "tía", "primo", "prima", "amigo", "amiga", "compañero", "compañera"]
    return random.choice(palabras)

def dar_pistas(palabra):
    inicio = palabra[0]
    final = palabra[-1]
    print(f"Pista: La palabra comienza con '{inicio}' y termina con '{final}'.")

def jugar_ahorcado():
    palabra = obtener_palabra_aleatoria()
    palabra_oculta = ['_'] * len(palabra)
    intentos_restantes = 7
    letras_utilizadas = []

    print("¡Bienvenido al juego de Ahorcado!")
    print("Adivina la palabra secreta. La palabra tiene", len(palabra), "letras.")
    dar_pistas(palabra)

    while intentos_restantes > 0 and '_' in palabra_oculta:
        print("Palabra secreta:", ' '.join(palabra_oculta))
        print("Intentos restantes:", intentos_restantes)
        letra = input("Ingresa una letra: ").lower()

        if letra in letras_utilizadas:
            print("Ya has utilizado esa letra. Intenta con otra.")
            continue

        letras_utilizadas.append(letra)

        if letra in palabra:
            print("¡Correcto! La letra", letra, "está en la palabra.")
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    palabra_oculta[i] = letra
        else:
            print("Incorrecto. La letra", letra, "no está en la palabra.")
            intentos_restantes -= 1

    if '_' not in palabra_oculta:
        print("¡Felicidades! ¡Has adivinado la palabra! La palabra era:", palabra)
    else:
        print("Lo siento, has agotado tus intentos. La palabra era:", palabra)

    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (sí/no): ")
    if jugar_de_nuevo.lower() == "sí":
        jugar_ahorcado()
    else:
        print("¡Gracias por jugar!")

if __name__ == "__main__":
    jugar_ahorcado()