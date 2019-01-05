FROM python:3.6-slim

WORKDIR /app
COPY . /app

RUN pip install poetry
RUN poetry config settings.virtualenvs.create false
RUN poetry install

CMD ["python", "src/index.py"]

