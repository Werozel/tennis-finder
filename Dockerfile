FROM python:3.10-slim

RUN apt update && apt upgrade -y

WORKDIR /code

COPY . /code/

RUN pip3 install -r requirements.txt

RUN pybabel compile -f -d tennis_finder/translations

RUN python3 tennis_finder/create_config.py

CMD ["python3", "-m", "tennis_finder"]