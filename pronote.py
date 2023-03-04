from pronotepy.ent import ent_elyco
import pronotepy
import datetime

import calendar



def get_homeworks(url, username, password):
    pronote = pronotepy.Client(
        pronote_url=url,
        username=username,
        password=password,
        ent=ent_elyco
    )
    today = datetime.date.today()
    days_ahead = (calendar.TUESDAY - today.weekday()) % 7
    next_tuesday = today + datetime.timedelta(days_ahead)
    tomorow = pronote.start_day + datetime.timedelta(days=1)

    if datetime.datetime.today().weekday() >= 4:
        homeworks = pronote.homework(date_from=today, date_to=next_tuesday)
    else:
        homeworks = pronote.homework(date_from=today, date_to=tomorow)

    dict_homeworks = {}
    for i in homeworks:
        dict_homeworks[i.subject.name] = (i.background_color) + "|" + i.description

    
    
    return dict_homeworks