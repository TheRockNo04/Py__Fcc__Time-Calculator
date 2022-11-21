def add_time(start, duration, day=""):
    start = start.replace(":", " ").split(" ")
    duration = duration.split(":")
    returnday = False
    retunrndaycount = False
    if day: returnday = True

    strhr = int(start[0])
    strmn = int(start[1])
    drhr = int(duration[0])
    drmn = int(duration[1])
    daycount = 0
    howmanydays = ""
    day = day.capitalize()

    strhr += drhr
    strmn += drmn

    while strhr>11 or strmn>59:
        if strhr > 11:
            strhr -= 12
            if start[2] == "PM":
                daycount += 1
                retunrndaycount = True
            start[2] = ampm(start[2])
        elif strmn > 59:
            strmn -= 60
            strhr += 1

    if strmn<10: strmn = f"0{str(strmn)}"

    if daycount == 1: howmanydays = "next day" 
    elif daycount > 1: howmanydays = f"{daycount} days later"
    if strhr == 0: strhr = 12
    if daycount: day = daychange(day, daycount)
    
    if returnday and retunrndaycount: new_time = f"{strhr}:{strmn} {start[2]}, {day} ({howmanydays})"
    elif retunrndaycount: new_time = f"{strhr}:{strmn} {start[2]} ({howmanydays})"
    elif returnday: new_time = f"{strhr}:{strmn} {start[2]}, {day}"
    else: new_time = f"{strhr}:{strmn} {start[2]}"
    
    return new_time

def ampm(amorpm):
    if amorpm == "AM": amorpm = "PM"
    elif amorpm == "PM": amorpm = "AM"
    return amorpm

def daychange(currday, daysskip):
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" ,"Sunday"]
    index = 0
    for i, e in enumerate(week):
        if currday == e:
            index = (i+daysskip)%7

    daynow = week[index]
    return daynow