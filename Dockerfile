FROM python:2.7

RUN pip install flask nose
ADD . /files/

CMD python /files/find_consecutive_runs.py
EXPOSE 5000