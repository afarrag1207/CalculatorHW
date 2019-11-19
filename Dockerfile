FROM python:3

ADD src /src

CMD [ "python", "./src/CSVTest.py" ]
