from datetime import datetime

def get_days_from_today(date):
    try:
        # make date from date string
        entry_date = datetime.strptime(date,'%Y-%m-%d')
        # find date difference
        date_delta = datetime.today() - entry_date
        # return difference // days only
        return date_delta.days
    except ValueError:
        return 'value error'

print(get_days_from_today('2024-09.19'))