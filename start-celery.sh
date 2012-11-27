#!/bin/bash

for i in {1..20}
do
	screen -dmS celery$i celery -A tasks worker --loglevel=info
done
