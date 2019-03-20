# Face Recognition

This repository contains the code for face recognition used in CaterPillar. This can be tested on a local machine using a webcam. The directory structure is as follow:

- dataset/ : Face dataset. Has a "unknown" folder that contains random faces. New folder is added to this directory whenever a new user is added.
- face_detection_model/ : Contains a pre-trained Caffe deep learning model provided by OpenCV to detect faces. This model detects and localizes faces in an image.
- output/ : contains output pickle files. 
- images/ : Test images will be uploaded here for recognition
- extract_embeddings.py : Extract images into 128D vector
- openface_nn4.small2.v1.t7: A Torch deep learning model which produces the 128-D facial embeddings
- train_model.py : Takes 128D vectors as input to train a linear SVM model for recognition
- recognize.py : Recognize images
- recognize_video.py : Recognize video
- collect_image.py : Starts the webcam and collect images of faces for training/recognition
