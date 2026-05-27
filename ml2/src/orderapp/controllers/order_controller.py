#cerate router for order service
from fastapi import APIRouter, FastAPI
from orderapp.dtos.order_request import OrderRequest    
from orderapp.dtos.order_response import OrderResponse
from orderapp.services.order_service_impl import OrderServiceImpl
import consul
from contextlib import asynccontextmanager
from orderapp.configurations.config import CONSUL_HOST, CONSUL_PORT, SERVICE_NAME_1, SERVICE_ID_1, SERVICE_HOST_1, SERVICE_NAME_1, SERVICE_PORT_1, SERVICE_NAME_2, SERVICE_ID_2, SERVICE_HOST_2, SERVICE_PORT_2
# --------------------------------
# Lifespan (startup + shutdown)
# --------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):

    # startup
    c = consul.Consul(
        host=CONSUL_HOST,
        port=CONSUL_PORT
    )

    c.agent.service.register(
        name=SERVICE_NAME_1,
        service_id=SERVICE_ID_1,
        address=SERVICE_HOST_1,
        port=SERVICE_PORT_1,
        check={
            "http": f"http://{SERVICE_HOST_1}:{SERVICE_PORT_1}/health",
            "interval": "10s",
            "timeout": "5s"
        }
    )

    print("✅ Order service registered with Consul")

    yield

    # shutdown
    c.agent.service.deregister(SERVICE_ID_1)

    print("❌ Order service deregistered")
app = FastAPI(title="Order Service", version="1.0.0", lifespan=lifespan)
@app.get("/health")
def health():
    return {
        "status": "UP"
    }


order_router = APIRouter(prefix="/orders", tags=["orders"])
order_service = OrderServiceImpl()
@order_router.post("/", response_model=OrderResponse)
def add_order(order_request:OrderRequest):
    return order_service.add_order(order_request)
@order_router.get("/", response_model=list[OrderResponse])
def get_all_orders():
    return order_service.get_all_orders()
@order_router.get("/{order_id}", response_model=OrderResponse)
def get_order_by_id(order_id: int):
    return order_service.get_order_by_id(order_id)
