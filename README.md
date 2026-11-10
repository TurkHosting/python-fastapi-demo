# python-fastapi-demo

FastAPI uygulaması. Paylaşımlı Plesk Python hostingte Passenger WSGI çalıştırdığı için uygulama `a2wsgi` ile sarılır (`passenger_wsgi.py`).

## Sınırlar
WebSocket ve uzun süren bağlantılar bu yolla desteklenmez (denenmedi, beklenmiyor). Bunlar için VDS gerekir.

## Uç noktalar
- `/` Framework ve Python sürümü
- `/health` Sağlık kontrolü
- `/items/{id}?q=...` Parametre testi
- `/docs` Swagger arayüzü

## Plesk'e yükleme
Flask demosuyla aynı adımlar: Scan, Enable Python, Create Virtual Environment, Install Dependencies, sayfayı yenile.
