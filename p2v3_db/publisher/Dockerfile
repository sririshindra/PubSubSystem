# Dockerfile - this is a comment. Delete me if you want.
FROM python:2.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
#ENTRYPOINT ["python"]
#CMD ["publisher.py 7001"]
#CMD ["subscriber.py 6001"]
#CMD ["broker.py 5000"]

#EXPOSE 5000
#
#EXPOSE 6000
#EXPOSE 6001
#EXPOSE 6002
#EXPOSE 6003
#EXPOSE 6004
#EXPOSE 6005
#
#EXPOSE 7000
#EXPOSE 7001
#EXPOSE 7002
#EXPOSE 7003
#EXPOSE 7004
#EXPOSE 7005

#CMD echo Hello world

EXPOSE 7000
ENTRYPOINT ["python"]
CMD ["publisher.py"]

#ENTRYPOINT ["sh"]
#CMD ["runfiles.sh"]
#CMD echo Hello rishi