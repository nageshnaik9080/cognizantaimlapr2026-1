import os
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), '..', '.env')

# Load environment variables from .env file
load_dotenv(env_path)

CONSUL_HOST = os.getenv("CONSUL_HOST")
CONSUL_PORT = int(os.getenv("CONSUL_PORT"))
SERVICE_NAME_1 = os.getenv("SERVICE_NAME_1")
SERVICE_ID_1= os.getenv("SERVICE_ID_1")
SERVICE_HOST_1 = os.getenv("SERVICE_HOST_1")
SERVICE_PORT_1 = int(os.getenv("SERVICE_PORT_1"))
SERVICE_NAME_2 = os.getenv("SERVICE_NAME_2")
SERVICE_ID_2= os.getenv("SERVICE_ID_2")
SERVICE_HOST_2 = os.getenv("SERVICE_HOST_2")
SERVICE_PORT_2 = int(os.getenv("SERVICE_PORT_2"))

