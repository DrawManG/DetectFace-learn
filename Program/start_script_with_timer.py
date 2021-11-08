from Program.average_definition import average_definition

def start_script_with_timer(timer,massive_name,anti_double_message):


    if timer == 500:
        massive_name,anti_double_message= average_definition(massive_name,anti_double_message)
        timer = 0
        whole_numb = 0
        massive_name = []
    if timer > 500:
        timer = 0
        whole_numb = 0
        massive_name = []