from Program.average_definition import average_definition
from Info_Base.informers import Time_Sending_a_message

def start_script_with_timer(timer,massive_name):


    if timer == Time_Sending_a_message:

        massive_name= average_definition(massive_name)
        timer = 0
        whole_numb = 0
        massive_name = []
    if timer > Time_Sending_a_message:
        timer = 0
        whole_numb = 0
        massive_name = []