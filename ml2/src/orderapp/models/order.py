import datetime

from sqlalchemy import Column, DateTime, Integer, DateTime, Boolean, Float
from orderapp.configurations.mysql_conf import base

from datetime import datetime
class Order(base):

    order_id:int=Column(Integer,primary_key=True,autoincrement=True)     
    customer_id:int=Column(Integer,default=0)
    #date of mysql datetime format
    order_date:datetime=Column(DateTime,default=datetime.today)
    order_status:bool=Column(Boolean,default=False)
    order_total:float=Column(Float,default=0.0)
