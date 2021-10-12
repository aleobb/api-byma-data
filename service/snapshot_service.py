
import os
from dotenv import load_dotenv
from homebroker import HomeBroker
import pandas as pd
from datetime import datetime

load_dotenv()

broker = os.getenv('Agent')
dni = os.getenv('Dni')
user = os.getenv('User')
password = os.getenv('Password')

def snapshot_service():
    try:
        hb = HomeBroker(int(broker))
        hb.auth.login(dni=dni, user=user, password=password, raise_exception=True)
        snapshot = hb.online.get_market_snapshot()
        '''date = '{}'.format(datetime.now().strftime('%Y%m%d'))
        for board in snapshot:
            snapshot[board].to_csv('{}_{}.csv'.format(date, board))'''
        date=[]
        for i in snapshot:
            df=pd.DataFrame(snapshot[i])
            date.append(df.to_json())
        message=date
        response={"status":"OK","message":message}
        print(response)
        return response
    except (os.error):
        message=os.error
        response={"status":"ERROR ","message":message}
        print(response)
        return response
