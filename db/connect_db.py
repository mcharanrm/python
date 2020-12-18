#!/usr/bin/env awx-python

import psycopg2
import sys;sys.path.append('/home/cmusali/private_zone/python')
from postgres import DATABASES

def find_max_id():
	db_connection = psycopg2.connect(user=DATABASES['default']['USER'],
	                                 password=DATABASES['default']['PASSWORD'],
					 host=DATABASES['default']['HOST'],
					 dbname=DATABASES['default']['NAME'])

	db_cursor = db_connection.cursor()
	db_cursor.execute("SELECT MAX(id) FROM main_jobevent")
	print("{}".format(db_cursor.fetchall()[0][0]))
	db_cursor.close()
	db_connection.close()

if globals()['__name__']=='__main__':
	find_max_id()
