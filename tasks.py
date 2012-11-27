from celery import Celery
import dns.resolver

celery = Celery('tasks', backend='redis://localhost', broker='amqp://')

@celery.task
def available (domain, tld):
	try:
		answer = dns.resolver.query(domain+"."+tld, 'SOA')
		return False
	except:
		return True