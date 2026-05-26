
from pydantic import BaseModel, Field

class Order_Response(BaseModel):
    order_id:int
    customer_id:int
    #date of mysql datetime format
    order_date: str
    order_status:bool
    order_total:float