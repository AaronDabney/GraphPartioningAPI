FROM nikolaik/python-nodejs:latest

USER root
WORKDIR /home/pn/app

COPY . .

RUN pip install numpy scikit-learn scipy
USER pn

EXPOSE 5000

CMD [ "node",  "server.js"]
