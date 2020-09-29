import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","Begineerproject.settings")



import django
django.setup()


## FAKE POP SCRIPT


import random
from firstAPP.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen=Faker()
topic=['Search','Social','Marketplace','News','Games']

def add_topic():

	t=Topic.objects.get_or_create(top_name=random.choice(topic))[0]
	t.save()
	return t

def populate(N=5):

	for entry in range(N):


		# get the topic from entry
		top=add_topic()

		# create fake data  for tht entry

		fake_name=fakegen.company()
		fake_url=fakegen.url()
		fake_date=fakegen.date()

		#create for webpage entry
		web_page=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

		#create fake Access
		acc_rec=AccessRecord.objects.get_or_create(name=web_page,date=fake_date)[0]

if __name__ == '__main__':
	print("Populating Script!")
	populate(20)
	print("Populating Complete")


