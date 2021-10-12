import os
from dotenv import load_dotenv
import datetime
from constant import convertDataToObjectDaily
from homebroker import HomeBroker

load_dotenv()

broker = os.getenv('Agent')
dni = os.getenv('Dni')
user = os.getenv('User')
password = os.getenv('Password')

def history_service(body):
    date_from_date=(datetime.datetime.strptime(body["date_from"], '%Y-%m-%d')).date()
    date_to_date=(datetime.datetime.strptime(body["date_to"], '%Y-%m-%d')).date()
    try:
        hb = HomeBroker(int(broker))
        hb.auth.login(dni=dni, user=user, password=password, raise_exception=True)
        data = hb.history.get_daily_history(body['symbol'],date_from_date, date_to_date)
        message=convertDataToObjectDaily(data,body['symbol'])
        response={"status":"OK","message":message}
        print(response)
        return response
    except (os.error):
        message=os.error
        response={"status":"ERROR ","message":message}
        print(response)
        return response
