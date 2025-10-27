# Battery Monitor — Тестовое задание

Сервис для мониторинга аккумуляторных батарей (АКБ) и устройств.  
Поддерживает CRUD-операции и привязку до 5 АКБ к одному устройству.

---

## 🚀 Запуск с Docker

1. Убедитесь, что установлены [Docker](https://www.docker.com/) и [Docker Compose](https://docs.docker.com/compose/).

2. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/kaelteritter/BatteriesDevices.git
   cd backend

3. Примените миграции:
```bash
cd backend
alembic upgrade head
```

4. Запустите сервер:
```bash
fastapi dev app/main.py --reload --port 8000
```
