FROM python:3.8
WORKDIR /
COPY requirements.txt /requirements.txt

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - &&\
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list &&\
    apt-get update  && ACCEPT_EULA=Y apt-get install -t stable -y msodbcsql17 unixodbc-dev --no-install-recommends &&\
    apt-get install -y python3-dev python3-distutils --no-install-recommends &&\
    pip install --no-cache-dir -r /requirements.txt &&\
    apt-get remove -y python3-dev python3-distutils gcc g++ && apt-get autoremove -y

RUN mkdir /linkedin/
RUN mkdir /env/

COPY . /linkedin
WORKDIR /env/

COPY env/. /env/

WORKDIR /linkedin/

CMD [ "python", "./main.py"]
MAINTAINER jparker@butlertill.com