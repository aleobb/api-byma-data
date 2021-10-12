from os import error
import sys

from service import quarter_service

sys.path.append("..")
from flask import  jsonify
from service import *

def quarter(symbol):
    try:        
        response=quarter_service(symbol['symbol'])
        res=jsonify({"succes":"true",'data': response })
        return res
    except(error):
        res=jsonify({"succes":"false",'data': error })
        return res
