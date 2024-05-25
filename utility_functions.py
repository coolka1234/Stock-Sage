from datetime import datetime
import pandas as pd
def date_to_ISO_8601(date):
    return date+'T00:00:00Z'

def return_relevant_date(date) -> bool:
    if 'T' in date:
        date=date.split('T')[0]
    date=pd.to_datetime(date)
    if date.weekday() ==5:
        return date+pd.Timedelta(days=2)
    elif date.weekday() ==6:
        return date+pd.Timedelta(days=1)
    return date

def change_date_format(date_string):
    dt = datetime.strptime(date_string, "%d/%m/%Y %H:%M")
    formatted_date = dt.strftime("%Y-%m-%dT%H:%M:%S")
    return formatted_date