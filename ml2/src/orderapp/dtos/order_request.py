import datetime

from pydantic import BaseModel,Field
from datetime import datetime
class OrderRequest(BaseModel):
    
    customer_id:int=Field(description="customer id foreign key")
    #date of mysql datetime format
    order_date:str=Field(description="order date")
    order_status:bool=Field(description="order status")
    order_total:float=Field(description="order total")
