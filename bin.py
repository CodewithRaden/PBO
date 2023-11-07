import cv2
import numpy as np

# Muat model klasifikasi wajah (misalnya, Haar Cascade)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Inisialisasi webcam
cap = cv2.VideoCapture(0)
# Initialize variables for motion detection
previous_frame = None

while True:
    # Capture the current frame
    ret, frame = cap.read()

    if not ret:
        break

    # Ubah frame menjadi grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Deteksi wajah dalam frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Gambar kotak di sekitar wajah yang terdeteksi
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Convert the frame to grayscale for motion detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Blur the grayscale frame to reduce noise
    gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    # Initialize the previous frame (first frame)
    if previous_frame is None:
        previous_frame = gray_frame
        continue

    # Calculate the absolute difference between the current and previous frames
    frame_diff = cv2.absdiff(previous_frame, gray_frame)

    # Apply a threshold to the difference frame
    _, thresh = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)

    # Dilate the thresholded image to fill in gaps
    thresh = cv2.dilate(thresh, None, iterations=2)

    # Find contours of the thresholded image
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw rectangles around moving objects
    for contour in contours:
        if cv2.contourArea(contour) > 1000:  # Adjust this value to set the minimum area for detection
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show the combined frame with face recognition and motion detection
    cv2.imshow('Face Recognition and Motion Detection', frame)

    # Store the current frame for the next iteration
    previous_frame = gray_frame

    # Hentikan loop jika pengguna menekan tombol 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Tutup webcam dan jendela tampilan
cap.release()
cv2.destroyAllWindows()
