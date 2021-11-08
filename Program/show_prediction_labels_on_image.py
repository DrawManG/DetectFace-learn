import numpy as np
from PIL import Image, ImageDraw

from Info_Base.informers import name_noBase_people,message_detect_NoBase_people,UTF
from Program.save_face_noname_detect import save_face_noname_detect
def show_prediction_labels_on_image(frame, predictions,whole_numb,name_massive,timer,anti_double_message):

    pil_image = Image.fromarray(frame)
    draw = ImageDraw.Draw(pil_image)

    for name, (top, right, bottom, left) in predictions:
        top *= 2
        right *= 2
        bottom *= 2
        left *= 2
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))


        if not name == None or not name == name_noBase_people:
            if whole_numb == 30 or timer==500:
                pass

            else:
                name_massive.append(name)
                if timer > 500:
                    timer = 0
                    whole_numb = 0
                    name_massive = []
            if name == name_noBase_people:
                print(whole_numb)
                if whole_numb < 30:
                    print(message_detect_NoBase_people)
                    save_face_noname_detect(frame)
                else:
                    whole_numb = 0





        name = name.encode(UTF)

        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
        draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))


    del draw
    opencvimage = np.array(pil_image)
    timer += 1
    whole_numb += 1


    return opencvimage,whole_numb,name_massive,timer