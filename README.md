ddac
====

distributed domain availability checker

## Installation of rabbitMQ, dnspython and Celery

<blockquote>
yum localinstall http://www.rabbitmq.com/releases/rabbitmq-server/v3.0.0/rabbitmq-server-3.0.0-1.noarch.rpm<br />
yum -y install python-pip python-dns.noarch python-celery.noarch screen<br />
/usr/bin/pip-python install -U Celery<br />
</blockquote>

## Starting the deamons

<blockquote>
/etc/init.d/rabbitmq-server start
cd ~/ddac
for i in {1..5}; do screen -dmS celery$i celery -A tasks worker --loglevel=info; done
</blockquote>