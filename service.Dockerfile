FROM python

COPY service.py /

RUN pip install bottle

CMD python3 service.py