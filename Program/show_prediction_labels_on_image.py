import numpy as np
from PIL import Image, ImageDraw

from Info_Base.informers import name_noBase_people,message_detect_NoBase_people,UTF,Time_Sending_a_message,whole
from Program.save_face_noname_detect import save_face_noname_detect
from PIL import ImageFont


def show_prediction_labels_on_image(frame, predictions,whole_numb,name_massive,timer):

    pil_image = Image.fromarray(frame)
    draw = ImageDraw.Draw(pil_image)

    for name, (top, right, bottom, left) in predictions:
        top *= 2
        right *= 2
        bottom *= 2
        left *= 2
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))


        if not name == None or not name == name_noBase_people:
            if whole_numb == whole or timer==Time_Sending_a_message:
                pass

            else:
                name_massive.append(name)
                if timer > Time_Sending_a_message:
                    timer = 0
                    name_massive = []
        if name == name_noBase_people:
                print(message_detect_NoBase_people)

                save_face_noname_detect(frame)








        name = name.encode(UTF)

        #font = ImageFont.truetype(size=40)


        text_width, text_height = draw.textsize(name)
        text_width *= 1
        text_height *= 1
        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))

        draw.text((left + 10, bottom - text_height - 5), text=name, fill=(255, 255, 255,255))


    del draw
    opencvimage = np.array(pil_image)
    timer += 1
    whole_numb += 1


    return opencvimage,whole_numb,name_massive,timer

def get_text_dimensions(text_string, font):

    ascent, descent = font.getmetrics()

    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent

    return (text_width, text_height)
