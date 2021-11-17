from Old_project.facerec_ipcamera_knn import *
from Info_Base.informers import path_file_learn,process_this_frame_procent,url_stream,resize_image,message

from Program.Train import train
from Info_Base.informers import process_this_frame as TEMP_process
from Program.show_prediction_labels_on_image import show_prediction_labels_on_image
from Program.start_script_with_timer import start_script_with_timer

def start_main():


    anti_double_message = 0
    timer = 0
    whole_numb = 0
    massive_name = []

    print(message[0])
    #classifier = train(path_train, model_save_path=path_file_learn, n_neighbors=n_neighbors)
    print(message[1])
    # 'http://username:password@camera_ip:port'
    url = url_stream

    cap = cv2.VideoCapture(0)
    process_this_frame = TEMP_process

    while 1 > 0:
        global global_caps
        caps = cap.read()
        ret, frame = caps
        cv2.imwrite('1.png', frame)
        if ret:
            img = cv2.resize(frame, resize_image[0], fx=resize_image[1], fy=resize_image[2])
            process_this_frame = process_this_frame + 1
            if process_this_frame % process_this_frame_procent == 0:
                predictions = predict(img, model_path=path_file_learn)
            frame,whole_numb,massive_name,timer = show_prediction_labels_on_image(frame, predictions,whole_numb,massive_name,timer)
            cv2.imshow('camera', frame)


            try:
                if timer>500:
                    massive_name = []
                    timer = 0

            except:
                pass


            start_script_with_timer(timer,massive_name,anti_double_message)






def test():
    anti_double_message = 0
    timer = 0
    whole_numb = 0
    massive_name = []
    process_this_frame = TEMP_process
    cap = cv2.VideoCapture(0)
    caps = cap.read()
    ret, frame = caps
    img = cv2.resize(frame, resize_image[0], fx=resize_image[1], fy=resize_image[2])
    process_this_frame = process_this_frame + 1
    if process_this_frame % process_this_frame_procent == 0:
        predictions = predict(img, model_path=path_file_learn)
    frame, whole_numb, massive_name, timer = show_prediction_labels_on_image(frame, predictions, whole_numb,
                                                                             massive_name, timer, anti_double_message)
    cv2.imshow('camera', frame)
    try:
        if timer > 500:
            massive_name = []
            timer = 0
            fire_frame = []
    except:
        pass

    return frame

start_main()







