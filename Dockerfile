FROM python:3.13-slim-bookworm

WORKDIR /app

COPY . .

RUN pip install poetry
RUN poetry install --no-root

EXPOSE 8000

ENTRYPOINT ["poetry", "run"]
CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000"]