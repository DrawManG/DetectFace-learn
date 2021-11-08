def save_face_noname_detect(frame):
    import os
    import datetime
    import cv2
    import random
    from Info_Base.informers import name_random,path_train

    path_project = os.getcwd()

    path_train = path_train
    folder_name = str(datetime.datetime.now()).split('.')[0].split(":")[0]

    if not os.path.isdir(path_train + folder_name):
        os.mkdir(path_train + folder_name)
    i = name_random
    cv2.imwrite(path_train + folder_name + "/" + str(i) + ".PNG", frame)
