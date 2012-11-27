ddac
====

distributed domain availability checker

## Installation of rabbitMQ, redis, dnspython and Celery

<blockquote>
yum localinstall http://www.rabbitmq.com/releases/rabbitmq-server/v3.0.0/rabbitmq-server-3.0.0-1.noarch.rpm<br />
yum -y install python-pip python-dns python-celery screen redis python-redis<br />
/usr/bin/pip-python install -U Celery<br />
</blockquote>

## Starting the deamons

<blockquote>
/etc/init.d/rabbitmq-server start<br />
/etc/init.d/redis start<br />
cd ~/ddac<br />
./start-celery.sh<br />
</blockquote>