FROM python:3.12-alpine3.17

ENV POETRY_VERSION=1.4.2

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

ENTRYPOINT [ "poetry", "run", "gunicorn", "-w", "4", "wsgi:app", "-b", "0.0.0.0:8000", "--log-level=debug" ]
