FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

COPY hello-world.py .

CMD ["python", "hello-world.py"]