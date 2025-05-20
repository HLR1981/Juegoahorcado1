import tkinter as tk
import random

# Lista de palabras
palabras = ["python", "ventana", "juego", "programa", "ahorcado", "computadora","teclado","mouse"]

# Selección de palabra al azar
palabra_secreta = random.choice(palabras)
letras_adivinadas = []
intentos_restantes = 6

# Función para actualizar la pantalla
def actualizar_pantalla():
    palabra_mostrada = " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra_secreta])
    palabra_label.config(text=palabra_mostrada)
    intentos_label.config(text=f"Intentos restantes: {intentos_restantes}")
    letras_label.config(text=f"Letras usadas: {' '.join(letras_adivinadas)}")

    if "_" not in palabra_mostrada:
        resultado_label.config(text="¡Ganaste!", fg="green")
        entrada.config(state="disabled")
        boton.config(state="disabled")
    elif intentos_restantes == 0:
        resultado_label.config(text=f"¡Perdiste! La palabra era: {palabra_secreta}", fg="red")
        entrada.config(state="disabled")
        boton.config(state="disabled")

# Función que maneja el intento del jugador
def intentar():
    global intentos_restantes
    letra = entrada.get().lower()
    entrada.delete(0, tk.END)

    if letra and letra.isalpha() and letra not in letras_adivinadas:
        letras_adivinadas.append(letra)
        if letra not in palabra_secreta:
            intentos_restantes -= 1
        actualizar_pantalla()

# Crear ventana
ventana = tk.Tk()
ventana.title("Juego del Ahorcado")
ventana.geometry("400x320")

# Etiquetas
palabra_label = tk.Label(ventana, font=("Arial", 20))
palabra_label.pack(pady=10)

intentos_label = tk.Label(ventana, text=f"Intentos restantes: {intentos_restantes}", font=("Arial", 12))
intentos_label.pack()

letras_label = tk.Label(ventana, text="Letras usadas:", font=("Arial", 12))
letras_label.pack()

resultado_label = tk.Label(ventana, font=("Arial", 14))
resultado_label.pack(pady=10)

# Entrada
entrada = tk.Entry(ventana, font=("Arial", 14), width=5, justify="center")
entrada.pack()
entrada.focus()

# Botón de intentar
boton = tk.Button(ventana, text="Intentar", command=intentar)
boton.pack(pady=5)

# Botón para salir del juego
boton_salir = tk.Button(ventana, text="Salir", command=ventana.destroy, fg="white", bg="red")
boton_salir.pack(pady=10)

# Iniciar pantalla
actualizar_pantalla()
ventana.mainloop()