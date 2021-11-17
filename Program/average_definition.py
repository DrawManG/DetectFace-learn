
from Info_Base.informers import name_noBase_people as namer_noname,message_telegram
def average_definition(name):
    import telegram_send
    '''

    ANTI_DOUBLE RELEASE DELETE

    :param name: massive
    :return: real name
    '''
    try:

        pre_realy = {i:name.count(i) for i in name}
        pre_realy1 = max(pre_realy.values())
        realistically_possible = list(pre_realy.keys())[list(pre_realy.values()).index(pre_realy1)]


    except:
        realistically_possible = namer_noname
    if not realistically_possible == namer_noname:
        telegram_send.send(messages=[message_telegram + realistically_possible])


    a = []
    return a