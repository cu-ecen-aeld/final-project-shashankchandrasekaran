##########################Importing libraries required for the program #############################
import face_recognition
import cv2
import numpy as np
import sys

###########################code for face recognition started##############################

file = '/home/capture_recreate.png'

# load the pictures whose faces have to be recognised.
harsh_image = face_recognition.load_image_file("/etc/face-rec-sample/photos/harsh.png")
harsh_image = cv2.resize(harsh_image, (0,0), fx =0.25, fy= 0.25)
harsh_face_encoding = face_recognition.face_encodings(harsh_image)[0]

shashank_image = face_recognition.load_image_file("/etc/face-rec-sample/photos/shashank.png")
shashank_image = cv2.resize(shashank_image, (0,0), fx =0.25, fy= 0.25)
shashank_face_encoding = face_recognition.face_encodings(shashank_image)[0]


# Load the image to be compared
unknown_image = face_recognition.load_image_file(file)
unknown_image = cv2.resize(unknown_image, (0,0), fx = 0.25, fy = 0.25)

# Find the face encodings for the unknown image
unknown_face_encodings = face_recognition.face_encodings(unknown_image)

# Compare the unknown face encodings with the known face encodings
try:
    results = face_recognition.compare_faces([harsh_face_encoding,shashank_face_encoding], unknown_face_encodings[0], tolerance =0.5)
except:
    print("No Match found")
    sys.exit(0)
# Print the results
if results[0]:
    print("Welcome home Harsh Beriwal")
    sys.exit(1)
elif results[1]:
    print("Welcome home Shashank Chandrasekaran")
    sys.exit(1)
else:
    print("No match found")
    sys.exit(0)

