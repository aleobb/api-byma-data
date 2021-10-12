from os import error
import sys

from service import history_service

sys.path.append("..")
from flask import  jsonify
from service import *

def history(body):
    try:        
        response=history_service(body)
        res=jsonify({"succes":"true",'data': response })
        return res
    except(error):
        res=jsonify({"succes":"false",'data': error })
        return res
