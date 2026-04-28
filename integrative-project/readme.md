# Orders Service

## Run

```bash
python -m uvicorn app.main:app --reload
python -m pytest -v
pip-audit
docker build -t orders-service .