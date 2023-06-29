FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /src

COPY . /src

COPY . .

RUN chmod a+x docker/*.sh

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install

RUN alembic upgrade head

EXPOSE 8001

CMD ["python", "./src/strart_up.py"]
