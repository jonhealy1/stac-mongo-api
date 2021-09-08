FROM python:3.7

RUN pip install fastapi uvicorn

EXPOSE 8000

COPY ./api /api

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]