FROM tensorflow/tensorflow

COPY models /app
COPY requirements.txt /app
COPY src/app/app.py /app

WORKDIR /app
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
EXPOSE 7860
CMD ["python", "app.py"]