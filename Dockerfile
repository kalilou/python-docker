FROM python:2.7-slim 
MAINTAINER KALILOU DIABY "kalilou1988@gmail.com"

COPY . /app 

WORKDIR /app 
RUN pip install -r requirement.txt 

ENTRYPOINT ["python"] 

CMD ["app.py"]  

