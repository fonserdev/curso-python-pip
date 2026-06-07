FROM python:3.8

WORKDIR /app
COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD bash -c "while true; do sleep 1; done;"
