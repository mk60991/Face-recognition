

# Import OpenCV2 for image processing
import cv2
import os

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

# Start capturing video 
vid_cam = cv2.VideoCapture(0)

# Detect object in video stream using Haarcascade Frontal Face
face_detector = cv2.CascadeClassifier('C:\\Users\\hp\\Downloads\\mAI-facerecpgnition\\Facereco\\haarcascade_frontalface_default.xml')

# For each person, one face id
#face_id = 1

# Initialize sample face image
#count = 0

Id=input('enter your id')
sampleNum=0

assure_path_exists("C:\\Users\\hp\\Downloads\\mAI-facerecpgnition\\Facereco\\dataset/")

# Start looping
while(True):

    # Capture video frame
    _, image_frame = vid_cam.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

    # Detect frames of different sizes, list of faces rectangles
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # Loops for each faces
    for (x,y,w,h) in faces:

        # Crop the image frame into rectangle
        cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)
        
        # Increment sample face image
        #count += 1
        sampleNum=sampleNum+1

        # Save the captured image into the datasets folder
        cv2.imwrite("C:\\Users\\hp\\Downloads\\mAI-facerecpgnition\\Facereco\\dataset/User." + str(Id) + '.' + str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])

        # Display the video frame, with bounded rectangle on the person's face
        cv2.imshow('frame', image_frame)

    # To stop taking video, press 'q' for at least 100ms
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

    # If image taken reach 100, stop taking video
    elif sampleNum>50:
        break

# Stop video
vid_cam.release()

# Close all started windows
cv2.destroyAllWindows()
