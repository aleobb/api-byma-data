from os import error
import sys

from service import snapshot_service

sys.path.append("..")
from flask import  jsonify
from service import *

def snapshot():
    try:        
        response=snapshot_service()
        res=jsonify({"succes":"true",'data': response })
        return res
    except(error):
        res=jsonify({"succes":"false",'data': error })
        return res
