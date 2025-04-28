# ---------------------------------------
# Programa en Python con OpenCV para:
# - Capturar video en vivo desde la cámara
# - Detectar contornos con findContours()
# - Dibujar contornos con drawContours()
# ---------------------------------------

import cv2

# Inicializar la cámara
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("No se pudo abrir la cámara")
    exit()

# Bajar la resolución para mejor rendimiento en Raspberry
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error al capturar el frame")
        break

    # Convertir el frame a escala de grises
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Aplicar un umbral binario para detectar objetos
    _, binaria = cv2.threshold(gris, 100, 255, cv2.THRESH_BINARY)

    # Encontrar contornos
    contornos, _ = cv2.findContours(binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar contornos sobre el frame original
    frame_contornos = frame.copy()
    cv2.drawContours(frame_contornos, contornos, -1, (0, 255, 0), 2)  # Color verde, grosor 2

    # Mostrar el frame con los contornos
    cv2.imshow('Contornos en Vivo', frame_contornos)

    # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
