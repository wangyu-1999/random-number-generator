FROM python:3.9

WORKDIR /code

COPY app.py .

RUN pip install gradio

EXPOSE 7860

CMD ["python", "app.py"]