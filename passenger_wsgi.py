# Passenger WSGI çalıştırır; FastAPI ASGI olduğu için a2wsgi ile sarılır.
from a2wsgi import ASGIMiddleware

from main import app

application = ASGIMiddleware(app)
