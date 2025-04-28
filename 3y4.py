import cv2
import os

class WebcamCapture:
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        self.image_count = 0
        self.capture_dir = 'Captures'
        os.makedirs(self.capture_dir, exist_ok=True)

    def capture_frame(self, frame):
        self.image_count += 1
        filename = os.path.join(self.capture_dir, f'image{self.image_count}.jpg')
        cv2.imwrite(filename, frame)
        print(f'Imagen guardada: {filename}')

    def process_last_image(self):
        if self.image_count == 0:
            print("No se capturaron imágenes para procesar.")
            return

        filename = os.path.join(self.capture_dir, f'image{self.image_count}.jpg')
        image = cv2.imread(filename)
        if image is None:
            print("Error al leer la imagen.")
            return

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        height, width = gray.shape
        mid_x, mid_y = width // 2, height // 2

        top_left = gray[0:mid_y, 0:mid_x]
        top_right = gray[0:mid_y, mid_x:width]
        bottom_left = gray[mid_y:height, 0:mid_x]
        bottom_right = gray[mid_y:height, mid_x:width]

        cv2.imshow('Cuadrante Superior Izquierdo', top_left)
        cv2.imshow('Cuadrante Superior Derecho', top_right)
        cv2.imshow('Cuadrante Inferior Izquierdo', bottom_left)
        cv2.imshow('Cuadrante Inferior Derecho', bottom_right)

        print("Presiona cualquier tecla para cerrar las ventanas de los cuadrantes.")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def run(self):
        print("Presiona 'f' para capturar una imagen.")
        print("Presiona 'q' para salir y procesar la última imagen capturada.")

        while True:
            ret, frame = self.capture.read()
            if not ret:
                print("Error al capturar el frame.")
                break

            cv2.imshow('Vista en Vivo', frame)
            key = cv2.waitKey(1) & 0xFF

            if key == ord('f'):
                self.capture_frame(frame)
            elif key == ord('q'):
                break

        self.capture.release()
        cv2.destroyAllWindows()
        self.process_last_image()

if __name__ == "__main__":
    webcam = WebcamCapture()
    webcam.run()
