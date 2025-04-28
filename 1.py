# ---------------------------------------
# Programa en Python con OpenCV para:
# - Cargar y reproducir un video
# - Redimensionarlo a 400x600 (ancho x alto)
# - Aplicar detector de bordes (Canny)
# - Dividir en mitades y cuadrantes
# - Mostrar cada uno en su propia ventana
# ---------------------------------------

import cv2

# Cargar el video
video = cv2.VideoCapture('sample_640x360.mp4')

if not video.isOpened():
    print("Error al abrir el video")
    exit()

while True:
    ret, frame = video.read()
    if not ret:
        print("Fin del video o error al leer el frame")
        break

    # Redimensionar el frame a 400x600 (ancho x alto)
    frame_resized = cv2.resize(frame, (400, 600))

    # Aplicar detector de bordes (Canny)
    edges = cv2.Canny(frame_resized, 100, 200)

    # Obtener mitad de ancho y mitad de alto
    mitad_ancho = frame_resized.shape[1] // 2
    mitad_alto = frame_resized.shape[0] // 2

    # Dividir en dos mitades
    izquierda = frame_resized[:, :mitad_ancho]
    derecha = frame_resized[:, mitad_ancho:]

    # Dividir en cuatro cuadrantes
    superior_izquierda = frame_resized[:mitad_alto, :mitad_ancho]
    superior_derecha = frame_resized[:mitad_alto, mitad_ancho:]
    inferior_izquierda = frame_resized[mitad_alto:, :mitad_ancho]
    inferior_derecha = frame_resized[mitad_alto:, mitad_ancho:]

    # Mostrar todas las ventanas
    cv2.imshow('Video Original', frame_resized)
    cv2.imshow('Detector de Bordes', edges)
    cv2.imshow('Mitad Izquierda', izquierda)
    cv2.imshow('Mitad Derecha', derecha)
    cv2.imshow('Cuadrante Superior Izquierda', superior_izquierda)
    cv2.imshow('Cuadrante Superior Derecha', superior_derecha)
    cv2.imshow('Cuadrante Inferior Izquierda', inferior_izquierda)
    cv2.imshow('Cuadrante Inferior Derecha', inferior_derecha)

    # Esperar 25 ms y salir si se presiona la tecla 'q'
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Liberar recursos
video.release()
cv2.destroyAllWindows()
