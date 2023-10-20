import os
import string
import cv2

# Define the directory where the data will be saved
DATA_DIR = "C:/Users/harsh/Desktop/ASL_Final1/data"

# Create the data directory if it doesn't exist
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Define the number of classes and the size of the dataset per class
number_of_classes = 27
dataset_size = 100
# Initialize the camera capture object (assuming camera index 2)
cap = cv2.VideoCapture(0)


for i in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(i))):
        os.makedirs(os.path.join(DATA_DIR, str(i)))

# Loop through each class
for j in range(number_of_classes):
    # Create a directory for the current class if it doesn't exist
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Collecting data for class {}'.format(j))

    # Display a message to instruct the user to press 'Q' to start capturing
    done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)

        # Wait for the user to press 'Q' to start capturing
        if cv2.waitKey(25) == ord('q'):
            break

    # Capture frames for the current class
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)

        # Save the captured frame to the corresponding class directory
        cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)

        counter += 1

# Release the camera and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
