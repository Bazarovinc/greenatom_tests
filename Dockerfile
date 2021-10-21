FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY poetry.lock pyproject.toml /app/
RUN pip3 install poetry
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --with-credentials
RUN pip3 install -r requirements.txt
COPY . /app/
RUN chmod 777 entrypoint.sh
RUN ./entrypoint.sh
RUN uvicorn main:app --reload --host 0.0.0.0
