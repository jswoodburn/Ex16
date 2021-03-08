from datetime import date


def validate_user_date(user_date, is_date_in_past=True):
    # validate format
    if len(str(user_date)) != 10:
        return "Please type out the date in full: yyyy-mm-dd"
    for i, character in enumerate(user_date):
        if i in [0,1,2,3,5,6,8,9] and character.isdecimal() == False:
            return "Please enter your date using numbers, in the format: yyyy-dd-mm."
        elif i in [4,7] and character != "-":
            return "Please use hyphens to when entering your date. e.g. yyyy-dd-mm"

    # validate date is in the past/future
    today = date.today()
    if is_date_in_past:
        if today.year < int(user_date[:4]):
            return "Please enter a date in the past."
        elif today.year == int(user_date[:4]):
            if today.month < int(user_date[5:7]):
                return "Please enter a date in the past."
            elif today.month == int(user_date[5:7]):
                if today.day <= int(user_date[8:]):
                    return "Please enter a date in the past."
    else:
        if today.year > int(user_date[:4]):
            return "Please enter a date in the future."
        elif today.year == int(user_date[:4]):
            if today.month > int(user_date[5:7]):
                return "Please enter a date in the future."
            elif today.month == int(user_date[5:7]):
                if today.day >= int(user_date[8:]):
                    return "Please enter a date in the future."

    return True
