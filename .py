import cv2
import tkinter as tk
import time

# Cargar los clasificadores
body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
eyepairsmall = cv2.CascadeClassifier('haarcascade_mcs_eyepair_small.xml')
eyepairbig = cv2.CascadeClassifier('haarcascade_mcs_eyepair_big.xml')
mcsleftear = cv2.CascadeClassifier('haarcascade_mcs_leftear.xml')
mcslefteye = cv2.CascadeClassifier('haarcascade_mcs_lefteye.xml')
mouth = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
rightear = cv2.CascadeClassifier('haarcascade_mcs_rightear.xml')
profileface = cv2.CascadeClassifier('haarcascade_profileface.xml')
righteyes = cv2.CascadeClassifier('haarcascade_righteye_2splits.xml')
smile = cv2.CascadeClassifier('haarcascade_smile.xml')
upperbydu = cv2.CascadeClassifier('haarcascade_upperbody.xml')
eyetree = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
eye = cv2.CascadeClassifier('haarcascade_eye.xml')
frontaltree = cv2.CascadeClassifier('haarcascade_frontalface_alt_tree.xml')
frontalalt = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
frontalalt2 = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
frontaldefault = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
lefteye = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')
lowerbody = cv2.CascadeClassifier('haarcascade_lowerbody.xml')

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
green_duration = 30  # Duración en segundos para mantener el semáforo en verde



# Iniciar el ciclo de cambios de color y detección de cuerpo
def detect_and_update():
    global start_time

    ret, img = cap.read()
    if not ret:
        window.after(10, detect_and_update)  # Intentar nuevamente después de 10 ms
        return
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    body_detections = body_cascade.detectMultiScale(gray, 1.1, 1)
    #eyepairsmall_detections = eyepairsmall.detectMultiScale(gray, 1.1, 1)
    #eyepairbig_detections = eyepairbig.detectMultiScale(gray, 1.1, 1)
    #mcsleftear_detections = mcsleftear.detectMultiScale(gray, 1.1, 1)
    #mcslefteye_detections = mcslefteye.detectMultiScale(gray, 1.1, 1)
    #mouth_detections = mouth.detectMultiScale(gray, 1.1, 1)
    #rightear_detections = rightear.detectMultiScale(gray, 1.1, 1)
    profileface_detections = profileface.detectMultiScale(gray, 1.1, 1)
    #righteyes_detections = righteyes.detectMultiScale(gray, 1.1, 1)
    #smile_detections = smile.detectMultiScale(gray, 1.1, 1)
    upperbody_detections = upperbydu.detectMultiScale(gray, 1.1, 1)
    #eyetree_detections = eyetree.detectMultiScale(gray, 1.1, 1)
    #eye_detections = eye.detectMultiScale(gray, 1.1, 1)
    frontaltree_detections = frontaltree.detectMultiScale(gray, 1.1, 1)
    frontalalt_detections = frontalalt.detectMultiScale(gray, 1.1, 1)
    frontalalt2_detections = frontalalt2.detectMultiScale(gray, 1.1, 1)
    frontaldefault_detections = frontaldefault.detectMultiScale(gray, 1.1, 1)
    #lefteye_detections = lefteye.detectMultiScale(gray, 1.1, 1)
    lowerbody_detections = lowerbody.detectMultiScale(gray, 1.1, 1)
    
    for (x, y, w, h) in body_detections:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    for (x, y, w, h) in profileface_detections:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    for (x, y, w, h) in upperbody_detections:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    for (x, y, w, h) in frontaltree_detections:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    for (x, y, w, h) in frontalalt_detections:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    for (x, y, w, h) in frontalalt2_detections:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    for (x, y, w, h) in frontaldefault_detections:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    for (x, y, w, h) in lowerbody_detections:
         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    if len(body_detections) > 0:
        turn_on_red()
        start_time = time.time()  # Reiniciar el tiempo cuando se detecta algo
    elif time.time() - start_time >= green_duration:
        turn_on_red()
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
