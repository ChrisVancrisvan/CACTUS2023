import cv2
import tkinter as tk
import time

# Cargar los clasificadores
classifiers = [
    'haarcascade_fullbody.xml',
    'haarcascade_profileface.xml',
    'haarcascade_upperbody.xml',
    'haarcascade_frontalface_alt_tree.xml',
    'haarcascade_frontalface_alt.xml',
    'haarcascade_frontalface_alt2.xml',
    'haarcascade_frontalface_default.xml',
    'haarcascade_lowerbody.xml'
]

cascades = [cv2.CascadeClassifier(cascade) for cascade in classifiers]

# Crear la ventana principal
window = tk.Tk()
window.title("Semáforo Simulado")
window.geometry("400x400")

# Crear los elementos del semáforo
canvas = tk.Canvas(window, width=150, height=500)
canvas.pack()

red_light = canvas.create_oval(25, 25, 125, 125, fill="gray")
yellow_light = canvas.create_oval(25, 150, 125, 250, fill="gray")
green_light = canvas.create_oval(25, 275, 125, 375, fill="gray")

# Funciones para cambiar el estado del semáforo
def turn_on_red():
    canvas.itemconfig(red_light, fill="red")
    canvas.itemconfig(yellow_light, fill="gray")
    canvas.itemconfig(green_light, fill="gray")

def turn_on_yellow():
    canvas.itemconfig(red_light, fill="gray")
    canvas.itemconfig(yellow_light, fill="yellow")
    canvas.itemconfig(green_light, fill="gray")

def turn_on_green():
    canvas.itemconfig(red_light, fill="gray")
    canvas.itemconfig(yellow_light, fill="gray")
    canvas.itemconfig(green_light, fill="green")

# Inicializar la captura de video desde la cámara predeterminada (índice 0)
cap = cv2.VideoCapture(1)

# Variables para controlar el tiempo
start_time = 0
red_duration = 5  # Duración en segundos para mantener el semáforo en rojo
green_duration = 30  # Duración en segundos para mantener el semáforo en verde
cycle_duration = 10  # Duración en segundos de cada ciclo

# Iniciar el ciclo de cambios de color y detección de cuerpo
def detect_and_update():
    global start_time

    ret, img = cap.read()
    if not ret:
        window.after(10, detect_and_update)  # Intentar nuevamente después de 10 ms
        return
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detections = []

    for cascade in cascades:
        cascade_detections = cascade.detectMultiScale(gray, 1.1, 1)
        detections.extend(cascade_detections)

    for (x, y, w, h) in detections:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    if len(detections) > 0:
        turn_on_red()
        start_time = time.time()  # Reiniciar el tiempo cuando se detecta algo
    elif time.time() - start_time >= red_duration:
        turn_on_green()
    else:
        turn_on_green()

    cv2.imshow('Camera', img)
    k = cv2.waitKey(30)
    if k == 27:  # Presionar Esc para salir
        cap.release()
        cv2.destroyAllWindows()
        window.destroy()
    else:
        window.after(10, detect_and_update)  # Llamar a la función cada 10 ms

# Ejecutar la función para iniciar el ciclo de cambios de color y detección de cuerpo
detect_and_update()

# Ejecutar la aplicación
window.mainloop()
