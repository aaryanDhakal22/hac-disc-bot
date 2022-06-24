from datetime import datetime
import pytz
TIMEZONE = "EST5EDT"
def timezone_est_datetime(hour,minute,day,month):
    result = pytz.timezone(TIMEZONE).localize(datetime(year=2022,month=month,day=day,hour=hour,minute=minute,second=0))
    return result

def return_schedule_for_stored():
    sc_file = open("./assets/schedule_list.txt", "r")
    sc_content = sc_file.readlines()
    schedules = []
    for item in sc_content:
        counter = 0
        schedule =item.strip().split()

        if schedule[0] == "(event)":
            event = True
            counter+=1
        else:
            event = False

        name = schedule[0+counter]
        time = schedule[2+counter]

        name = " ".join(name.split("_"))
        meridian = time[-2:].strip()
        colon_on = time.find(":")
        hour = int(time[:colon_on])
        if meridian == "PM":
            if hour!=12:
                hour+=12
            else:
                pass
        if meridian=="AM" and hour=="12":
            hour=0
        minute = int(time[colon_on+1:colon_on+3])
        day = int(schedule[-1])
        month = int(schedule[-2])
        new_dict = dict(name=name,event=event,datetime=timezone_est_datetime(hour,minute,day,month))
        schedules.append(new_dict)
    sc_file.close()
    return schedules

return_schedule_for_stored()