FROM python:2.7.10

ENV APP_HOME /blog
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

ADD requirements.txt $APP_HOME/
RUN pip install -r requirements.txt

ADD . $APP_HOME
