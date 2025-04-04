FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py migrate --noinput

RUN python manage.py collectstatic --noinput

EXPOSE 8050

CMD ["gunicorn", "Cinema.wsgi:application", "--bind", "0.0.0.0:8050"]
