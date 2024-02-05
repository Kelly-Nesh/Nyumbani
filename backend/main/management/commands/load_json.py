import json
import time
from random import sample, choice
import concurrent.futures as cf
from django.core.management.base import BaseCommand
from main import models as m
from data.mock_town_data import towns
from data.mock_agent_data import agents
from data.mock_house_data import houses
from data.mock_user_data import users


class Command(BaseCommand):
	house_data = houses
	town_objs = ''
	agent_objs = ''
	suburb_objs = ''
	user_objs = ''

	def handle(self, *args, **kwargs):
		start = time.time()
		pool = cf.ThreadPoolExecutor(max_workers=4)
		print(pool.submit(self.get_load_towns), time.time())
		print(pool.submit(self.get_load_agents), time.time())
		print(pool.submit(self.get_load_users), time.time())

		# wait for threads before main thread continues
		pool.shutdown(wait=True)
		print('{}'.format(time.time()-start))
		self.load_suburbs()
		self.load_houses()


	def get_load_towns(self):
		town_data_objs = [m.Town(name=t['name']) for t in towns]
		self.town_objs = m.Town.objects.bulk_create(town_data_objs)
		# print(self.town_objs)

	def get_load_agents(self):
		agent_suffixes = ['Investments', 'Finance', 'Sacco', 'Agents']
		self.agent_objs = [m.Agent.objects.get_or_create(name="{} {}".format(
			a['name'], choice(agent_suffixes)), phone_number=a['phone_number'])[0]
			for a in agents]

	def get_load_users(self):
		user_data_objs = [m.User(name=u['name']) for u in users]
		self.user_objs = m.User.objects.bulk_create(user_data_objs)
		# print(self.user_objs)

	def load_suburbs(self):
		suburbs_sample = sample(self.house_data, 35)
		suburbs_temp_objs = [m.Suburb(name=row['location'],
			town=choice(self.town_objs)) for row in suburbs_sample]
		self.suburb_objs = m.Suburb.objects.bulk_create(suburbs_temp_objs)
		# print(self.suburb_objs)

	def load_houses(self):
		house_objs = []
		house_suffixes = ['apartments', 'flats', 'heights', 'building', 'rentals']
		for row in self.house_data:
			name = "{} {}".format(row['name'], choice(house_suffixes))
			location = choice(self.suburb_objs)
			agent = choice(self.agent_objs)
			bedrooms = row['bedrooms']
			bathrooms = row['bathrooms']
			price = row['price']
			pets_allowed = row['pets_allowed']
			available = row['available']
			house_objs.append(m.House(name=name, location=location, agent=agent,
				bedrooms=bedrooms, price=price, pets_allowed=pets_allowed,
				bathrooms=bathrooms, available=available))
		m.House.objects.bulk_create(house_objs)
