import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Kamera tidak dapat diakses!")
    exit()

print("Program akan berhenti setelah 5 tangkapan.")

for i in range(5):
    ret, frame = camera.read()
    if ret:
        file_name = f"foto_{i+1}.jpg"
        cv2.imwrite(file_name, frame)
        print(f"Foto {i+1} berhasil diambil: {file_name}")
    else:
        print("Gagal mengambil foto!")

camera.release()
print("Program selesai.")