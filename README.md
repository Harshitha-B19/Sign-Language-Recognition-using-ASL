The challenge at hand is to develop a robust Sign Language Recognition (SLR) system for American Sign Language (ASL) that accurately recognizes and interprets ASL gestures, enabling real-time translation. This system aims to address the communication barriers faced by ASL users in education, employment, and daily interactions, thereby isolating speech-impaired individuals from mainstream society. The goal is to leverage technology to empower ASL users and create a more equitable and inclusive society. Furthermore, this system should integrate with various computer applications, enhancing accessibility and inclusivity, and ultimately bridging the gap between the speech-impaired and the broader community.


Order of execution:  
          collect_images.py-----collectes images for A-Z and Space
          create_dataset.py------converts collected images into dataset, which is further used during development. data.pickle file is generated.
          train_classifier.py-----creating the model, fiting and train the model using Random Forest Classifier. model.p file is generated.
          inference__classifier.py----imports model, creates the GUI using Tkinter.




OBJECTIVE OF THE PROJECT
•	To Develop a robust system that can accurately recognize American Sign Language (ASL) gestures in real-time using computer vision and machine learning techniques.
•	Create an intuitive graphical user interface (GUI) using Tkinter that allows users to interact with the system, providing instant feedback on the recognized signs.
•	Introduce a time delay between recognizing consecutive gestures to ensure that each gesture is captured individually and accurately. 
•	Offer users the functionality to save the recognized text to a text file, allowing them to review and reference their interactions later
