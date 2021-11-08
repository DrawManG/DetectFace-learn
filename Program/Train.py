import math
import os
import os.path
import os.path
import pickle

import face_recognition
from face_recognition.face_recognition_cli import image_files_in_folder
from sklearn import neighbors

from Info_Base.informers import message

def train(train_dir, model_save_path=None, n_neighbors=None, knn_algo='ball_tree', verbose=True):

    X = []
    y = []


    for class_dir in os.listdir(train_dir):
        if not os.path.isdir(os.path.join(train_dir, class_dir)):
            continue

        for img_path in image_files_in_folder(os.path.join(train_dir, class_dir)):
            image = face_recognition.load_image_file(img_path)
            face_bounding_boxes = face_recognition.face_locations(image)

            if len(face_bounding_boxes) != 1:
                if verbose:
                    print(message[2].format(img_path, message[3] if len(face_bounding_boxes) < 1 else message[4]))
            else:

                X.append(face_recognition.face_encodings(image, known_face_locations=face_bounding_boxes)[0])
                y.append(class_dir)

    if n_neighbors is None:
        n_neighbors = int(round(math.sqrt(len(X))))
        if verbose:
            print(message[5], n_neighbors)

    knn_clf = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors, algorithm=knn_algo, weights='distance')
    knn_clf.fit(X, y)

    if model_save_path is not None:
        with open(model_save_path, 'wb') as f:
            pickle.dump(knn_clf, f)

    return knn_clf