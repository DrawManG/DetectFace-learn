def save_face_noname_detect(frame):
    import os
    import datetime
    import cv2
    import random
    from Info_Base.informers import path_train2,path_project


    folder_name = str(datetime.datetime.now()).split('.')[0].split(":")[0].replace(" ","_")
    print(path_project + path_train2 + folder_name)
    if not os.path.isdir(path_project + path_train2 + folder_name):
        os.mkdir(path_project + path_train2 + folder_name)
    name_random = random.randint(0, 999999999)
    i = name_random
    cv2.imwrite(path_project + path_train2 + folder_name + "/" + str(i) + ".PNG", frame)
