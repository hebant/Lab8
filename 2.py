# ------------------------------------------------------
# Programa en Python con OpenCV (OOP) para:
# - Encender la cámara
# - Aplicar 1 de 3 filtros usando SOLO cvtColor
# - Mantener UNA sola ventana
# ------------------------------------------------------

import cv2

class CameraFilter:
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        
        # Bajar la resolución de la cámara a 640x480
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        self.filter_selected = 0  # 0: Normal, 1: Escala de grises, 2: Invertido, 3: HSV

        if not self.capture.isOpened():
            print("Error: No se pudo abrir la cámara.")
            exit()

    def apply_filter(self, frame):
        if self.filter_selected == 0:
            return frame  # Sin filtro
        elif self.filter_selected == 1:
            return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Escala de grises
        elif self.filter_selected == 2:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            inverted = cv2.bitwise_not(gray)  # Invertido en escala de grises
            return inverted
        elif self.filter_selected == 3:
            return cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Espacio de color HSV
        else:
            return frame

    def run(self):
        print("\nControles:")
        print("'0' -> Sin filtro")
        print("'1' -> Escala de Grises")
        print("'2' -> Invertido (Grises)")
        print("'3' -> Espacio de color HSV")
        print("'q' -> Salir\n")

        while True:
            ret, frame = self.capture.read()
            if not ret:
                print("Error al capturar el frame.")
                break

            filtered_frame = self.apply_filter(frame)

            # Si el frame es escala de grises o invertido, reconvertirlo a BGR para mostrar texto
            if len(filtered_frame.shape) == 2:
                filtered_frame = cv2.cvtColor(filtered_frame, cv2.COLOR_GRAY2BGR)

            # Mostrar el nombre del filtro
            filtro_texto = {
                0: "Normal",
                1: "Grises",
                2: "Invertido (Grises)",
                3: "HSV"
            }
            texto = filtro_texto.get(self.filter_selected, "Desconocido")

            # Dibujar el nombre del filtro
            cv2.putText(filtered_frame, f"Filtro: {texto}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            cv2.imshow('Camara con Filtros', filtered_frame)

            key = cv2.waitKey(1) & 0xFF

            if key == ord('q'):
                break
            elif key in [ord('0'), ord('1'), ord('2'), ord('3')]:
                self.filter_selected = int(chr(key))

        self.capture.release()
        cv2.destroyAllWindows()

# Ejecutar el programa
if __name__ == "__main__":
    cam_filter = CameraFilter()
    cam_filter.run()
