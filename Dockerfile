FROM python:3

WORKDIR /usr/src/app

COPY karnataka_tomato_price.csv .
COPY main.py .

RUN pip install pandas
RUN pip install sklearn
RUN pip install argparse

CMD ["python", "./main.py"]