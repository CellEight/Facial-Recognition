import cv2
import face_recognition
"""
# Load the cascade

face_cascade = cv2.CascadeClassifier('face_detector.xml')

img = cv2.imread('they are watching you.jpg')

faces = face_cascade.detectMultiScale(img, 1.1, 4)

for (x ,y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)

cv2.imwrite("output.png", img)
"""

know_image = face_recognition.load_image_file("person.jpg")
know_encoding = face_recognition.face_encodings(know_image)[0]
while True:
    # Grab a single frame of video
    ret, unknown_image = video_capture.read()
    #unknown_image = face_recognition.load_image_file("they are watching you.jpg")
    unknown_locations = face_recognition.face_locations(unknown_image)
    unknown_encodings = face_recognition.face_encodings(unknown_image, unknown_locations)
    i=1
    for (top, right, bottom, left), encoding in zip(unknown_locations,unknown_encodings):
        result = face_recognition.compare_faces([know_encoding], encoding)[0]
        if result:
            cv2.rectangle(unknown_image, (left,top), (right, bottom), (255,0,0), 1)
            cv2.rectangle(unknown_image, (left, bottom - 20), (right, bottom), (255, 0, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(unknown_image, "Snowden", (left + 6, bottom - 6), font, 0.35, (255, 255, 255), 1)
        else:
            cv2.rectangle(unknown_image, (left,top), (right, bottom), (255,0,0), 1)
            cv2.rectangle(unknown_image, (left, bottom - 20), (right, bottom), (255, 0, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(unknown_image, f"Suspect {i}", (left + 6, bottom - 6), font, 0.35, (255, 255, 255), 1)
        i += 1
    cv2.imgshow("output_labled_crowd.png",cv2.cvtColor(unknown_image,cv2.COLOR_BGR2RGB))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
