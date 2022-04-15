# Problem: https://www.hackerrank.com/challenges/python-time-delta/problem

from datetime import datetime as dt
# Complete the time_delta function below.
def time_delta(t1, t2):
    dt_fmt = '%a %d %b %Y %H:%M:%S %z'
    date1, date2 = dt.strptime(t1, dt_fmt), dt.strptime(t2, dt_fmt)
    return str(round(abs((date1-date2).total_seconds())))