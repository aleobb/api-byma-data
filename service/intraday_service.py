import os
from dotenv import load_dotenv
from constant import convertDataToObjectIntraday,convertDataMin
from homebroker import HomeBroker

load_dotenv()

broker = os.getenv('Agent')
dni = os.getenv('Dni')
user = os.getenv('User')
password = os.getenv('Password')

def intraday_service(symbol):
    try:            
        hb = HomeBroker(int(broker))
        hb.auth.login(dni=dni, user=user, password=password, raise_exception=True)
        data = hb.history.get_intraday_history(symbol, None, None)
        msg=convertDataToObjectIntraday(data,symbol)
        message=convertDataMin(msg)
        response={"status":"OK","message":message}
        print(response)
        return response
    except (os.error):
        message=os.error
        response={"status":"ERROR ","message":message}
        print(response)
        return response
