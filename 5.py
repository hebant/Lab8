# ---------------------------------------
# Programa en Python con OpenCV para:
# - Cargar una imagen
# - Detectar contornos usando findContours()
# - Dibujar los contornos usando drawContours()
# ---------------------------------------

import cv2

# Cargar la imagen
imagen = cv2.imread('manzana.jpg') 

if imagen is None:
    print("Error al cargar la imagen")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar un umbral para binarizar la imagen
_, umbral = cv2.threshold(gris, 127, 255, cv2.THRESH_BINARY)

# Encontrar contornos
contornos, jerarquia = cv2.findContours(umbral, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar los contornos sobre la imagen original
imagen_contornos = imagen.copy()
cv2.drawContours(imagen_contornos, contornos, -1, (0, 255, 0), 2)  # Color verde y grosor de 2 píxeles

# Mostrar la imagen original y la imagen con contornos
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen con Contornos', imagen_contornos)

# Esperar hasta que se presione una tecla
cv2.waitKey(0)
cv2.destroyAllWindows()
