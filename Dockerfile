FROM python:2.7

ADD ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt
ADD . /files/

CMD python /files/find_consecutive_runs.py
EXPOSE 5000