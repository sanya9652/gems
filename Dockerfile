FROM python:3.9

RUN mkdir -p /src/app/
WORKDIR /src/app/
COPY requirements.txt /src/app/

COPY src /src/app/
RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ['python', 'manage.py']