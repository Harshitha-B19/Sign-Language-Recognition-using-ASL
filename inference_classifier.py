import pickle
import cv2
import mediapipe as mp
import numpy as np
import tkinter as tk
import time
import os

model_dict = pickle.load(open("C:/Users/harsh/Desktop/ASL_Final1/model.p", 'rb'))
model = model_dict['model']

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

labels_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z', 26: ' '}

recognized_alphabet = ""
recognized_flag = False
start_time = time.time()
file_counter = 0

# Create a Tkinter window for displaying the final recognized text
root = tk.Tk()
root.title("ASL Recognizer")

# Create a frame for the video feed
video_frame = tk.Frame(root)
video_frame.pack(side="left")

# Create a label for the video feed
video_label = tk.Label(video_frame)
video_label.pack()

# Create a frame for the text widget
text_frame = tk.Frame(root)
text_frame.pack(side="right", fill="both", expand=True)

# Create a text widget for displaying recognized text
text_widget = tk.Text(text_frame, font=("Helvetica", 14))
text_widget.pack(fill="both", expand=True)

# Function to update recognized text
def update_text():
    recognized_text = "Final Recognized Text:\n" + recognized_alphabet
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, recognized_text)


def save_recognized_text():
    global file_counter, recognized_alphabet
    filename = f"recognized_text_{file_counter}.txt"
    with open(filename, "w") as text_file:
        text_file.write(recognized_alphabet)
    file_counter += 1
    recognized_alphabet = ""  # Clear the recognized text
    update_text()

# Create a button to save the recognized text
save_button = tk.Button(text_frame, text="Save", command=save_recognized_text)
save_button.pack(side="bottom")

# Create a button to close the window
close_button = tk.Button(text_frame, text="Close", command=root.destroy)
close_button.pack(side="bottom")

while True:
    data_aux = []
    x_ = []
    y_ = []

    ret, frame = cap.read()
    H, W, _ = frame.shape
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

        for hand_landmarks in results.multi_hand_landmarks:
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y

                x_.append(x)
                y_.append(y)

            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x - min(x_))
                data_aux.append(y - min(y_))

        x1 = int(min(x_) * W) - 10
        y1 = int(min(y_) * H) - 10

        x2 = int(max(x_) * W) - 10
        y2 = int(max(y_) * H) - 10

        prediction = model.predict([np.asarray(data_aux)])
        predicted_character = labels_dict[int(prediction[0])]

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
        cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                    cv2.LINE_AA)

        # Update recognized_alphabet
        if not recognized_flag:
            recognized_alphabet += predicted_character
            recognized_flag = True

        # Check if 2 seconds have passed
        elapsed_time = time.time() - start_time
        if elapsed_time >= 3:
            recognized_flag = False
            start_time = time.time()

    # Convert the frame to a format suitable for displaying in Tkinter
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = tk.PhotoImage(data=cv2.imencode('.png', frame)[1].tobytes())

    # Update the video feed label
    video_label.configure(image=img)
    video_label.image = img

    # Update the text widget with recognized text
    update_text()

    root.update()  # Update the Tkinter window

cap.release()
cv2.destroyAllWindows()

root.mainloop()
