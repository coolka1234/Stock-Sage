import datetime
import pandas as pd
import yfinance as yf
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
    dt = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M")
    formatted_date = dt.strftime("%Y-%m-%dT%H:%M:%S")
    return formatted_date

def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""
def get_company_name(symbol):
    ticker = yf.Ticker(symbol)
    return ticker.info['longName']

import os
import sys
def resource_path(relative_path):
    """ Get absolute path to resource, works for both dev and PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def resource_path_gp(relative_path):
    """ Get absolute path to resource, works for both dev and PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)