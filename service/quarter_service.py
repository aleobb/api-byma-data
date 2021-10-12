import os
from dotenv import load_dotenv
from constant import convertDataToObjectDaily
from homebroker import HomeBroker
from datetime import date
import datetime

load_dotenv()

broker = os.getenv('Agent')
dni = os.getenv('Dni')
user = os.getenv('User')
password = os.getenv('Password')

def quarter_service(symbol):
    today = date.today()
    year=int(today.strftime("%Y"))
    if(int(today.strftime("%m"))==4):
        month=12
    elif(int(today.strftime("%m"))==3):
        month=11
    elif(int(today.strftime("%m"))==2):
        month=10
    elif(int(today.strftime("%m"))==1):
        month=9
    else:
        month=int(today.strftime("%m"))-4
    day=int(today.strftime("%d"))
    try:            
        hb = HomeBroker(int(broker))
        hb.auth.login(dni=dni, user=user, password=password, raise_exception=True)
        data = hb.history.get_daily_history(symbol,(datetime.date(year, month, day)), today)
        message=convertDataToObjectDaily(data,symbol)
        response={"status":"OK","message":message}
        print(response)
        return response
    except (os.error):
        message=os.error
        response={"status":"ERROR ","message":message}
        print(response)
        return response
