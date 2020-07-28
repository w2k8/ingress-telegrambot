import telebot
import sqlite3
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os
import time
import logging

logging.basicConfig(format='%(asctime)s %(message)s')
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

bot = telebot.TeleBot("Youre_bot_api")

agent_stats_objects = [ 'Time Span',  							#1
						'Agent Name', 							#2
						'Agent Faction',						#3
						'Date',									#4
						'Time',									#5
						'Level',								#6
						'Lifetime AP',							#7
						'Current AP',							#8
						'Unique Portals Visited',				#9
						'Unique Portals Drone Visited',			#10
						'Furthest Drone Flight Distance',		#11
						'Portals Discovered',					#12
						'XM Collected',							#13
						'OPR Agreements',						#14
						'Portal Scans Uploaded',				#15
						'Scout Controller on Unique Portals',	#16
						'Distance Walked',						#17
						'Resonators Deployed',					#18
						'Links Created',						#19
						'Control Fields Created',				#20
						'Mind Units Captured',					#21
						'Longest Link Ever Created',			#22
						'Largest Control Field',				#23
						'XM Recharged',							#24
						'Portals Captured',						#25
						'Unique Portals Captured',				#26
						'Mods Deployed',						#27
						'Resonators Destroyed',					#28
						'Portals Neutralized',					#29
						'Enemy Links Destroyed',				#30
						'Enemy Fields Destroyed',				#31
						'Max Time Portal Held',					#32
						'Max Time Link Maintained',				#33
						'Max Link Length x Days',				#34
						'Max Time Field Held',					#35
						'Largest Field MUs x Days',				#36
						'Forced Drone Recalls',					#37
						'Unique Missions Completed',			#38
						'Hacks',								#39
						'Drone Hacks',							#40
						'Glyph Hack Points',					#41
						'Longest Hacking Streak',				#42
						'Agents Successfully Recruited',		#43
						'Mission Day(s) Attended',				#44
						'NL-1331 Meetup(s) Attended',			#45
						'First Saturday Events',				#46
						'Recursions']							#47


def init_db():
	conn = sqlite3.connect('agent_stats.db')
	c = conn.cursor()
	# Create table
	c.execute('''CREATE TABLE agents_stats
				('agent_telegram_id',
				'Time Span',
				'Agent Name',
				'Agent Faction',
				'Date',
				'Time',
				'Level',
				'Lifetime AP',
				'Current AP',
				'Unique Portals Visited',
				'Unique Portals Drone Visited',
				'Furthest Drone Flight Distance',
				'Portals Discovered',
				'XM Collected',
				'OPR Agreements',
				'Portal Scans Uploaded',
				'Scout Controller on Unique Portals',
				'Distance Walked',
				'Resonators Deployed',
				'Links Created',
				'Control Fields Created',
				'Mind Units Captured',
				'Longest Link Ever Created',
				'Largest Control Field',
				'XM Recharged',
				'Portals Captured',
				'Unique Portals Captured',
				'Mods Deployed',
				'Resonators Destroyed',
				'Portals Neutralized',
				'Enemy Links Destroyed',
				'Enemy Fields Destroyed',
				'Max Time Portal Held',
				'Max Time Link Maintained',
				'Max Link Length x Days',
				'Max Time Field Held',
				'Largest Field MUs x Days',
				'Forced Drone Recalls',
				'Unique Missions Completed',
				'Hacks',
				'Drone Hacks',
				'Glyph Hack Points',
				'Longest Hacking Streak',
				'Agents Successfully Recruited',
				'Mission Day(s) Attended',
				'NL-1331 Meetup(s) Attended',
				'First Saturday Events',
				'Recursions')''')
	# Save (commit) the changes and close the connection
	conn.commit()
	conn.close()


def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	cid = message.chat.id
	log.debug("Before send start")
	bot.send_message(cid, "Ingress Agent Stats bot")
	log.debug("After send start")


@bot.message_handler(commands=['stats', 'help'])
def send_stats(message):
	cid = message.chat.id
	agent_telegram_id = message.from_user.id

	conn = sqlite3.connect('agent_stats.db')
	c = conn.cursor()
	player_ap = []
	player_resonator_deployed = []
	player_links_created = []
	player_control_field_created = []
	player_recharged = []

	stats_date = []
	for row in c.execute("SELECT * FROM agents_stats WHERE agent_telegram_id={}".format(agent_telegram_id)):
		stats_date.append('{} {}'.format(row[4], row[5]))
		player_ap.append(row[8])
		player_resonator_deployed.append(row[17])
		player_links_created.append(row[18])
		player_control_field_created.append(row[19])
		player_recharged.append(row[24])
	conn.close()
	player_name = row[2]

	fig, ax1 = plt.subplots()

	#Create plot title
	ax1.set_title("Ingress player stats: {}".format(player_name))

	# Create the label for the x-as and rotate the label 45 degrease
	ax1.set_xlabel('Time')
	ax1.tick_params('x', labelrotation=45)

	# Create the first label for the y-as
	# This should be the player AP, the color is blue
	ax1.tick_params('y', colors='b')
	ax1.plot(stats_date,player_ap, 'b-')
	ax1.set_ylabel('Player AP', color='b')

	ax2 = ax1.twinx()
	# Create the second label for the y-as
	# This should be some other stats, the color is red
	ax2.tick_params('y', colors='r')
	ax2.plot(stats_date,player_resonator_deployed, 'r-')
	ax2.set_ylabel('Resonators deployed', color='r')

	fig.tight_layout()
	# plt.show()
	try:
		os.remove('images/{}.png'.format(cid))
	except:
		pass
	plt.savefig('images/{}.png'.format(cid))
	img = open('images/{}.png'.format(cid), 'rb')
	log.debug("Before send stats")
	bot.send_photo(cid, img)
	log.debug("after send stats")
	try:
		os.remove('images/{}.png'.format(cid))
	except:
		pass
	# Create the second plot with stats

	fig, ax1 = plt.subplots()

	#Create plot title
	ax1.set_title("Ingress player stats: {}".format(player_name))

	# Create the label for the x-as and rotate the label 45 degrease
	ax1.set_xlabel('Time')
	ax1.tick_params('x', labelrotation=45)

	# Create the first label for the y-as
	# This should be the player stats, the color is blue
	ax1.tick_params('y', colors='b')
	ax1.plot(stats_date,player_links_created, 'b-')
	ax1.set_ylabel('Linkes created', color='b')

	ax2 = ax1.twinx()
	# Create the second label for the y-as
	# This should be some other stats, the color is red
	ax2.tick_params('y', colors='r')
	ax2.plot(stats_date,player_control_field_created, 'r-')
	ax2.set_ylabel('Control field created', color='r')

	fig.tight_layout()

	# Save the plot, send it and delete the plot.
	# Just not sure how the send the plot as image object directly
	try:
		os.remove('images/{}.png'.format(cid))
	except:
		pass	
	plt.savefig('images/{}.png'.format(cid))
	img = open('images/{}.png'.format(cid), 'rb')
	log.debug("Before send stats")
	bot.send_photo(cid, img)
	log.debug("After send stats")
	try:
		os.remove('images/{}.png'.format(cid))
	except:
		pass

	plt.clf()
	plt.title("Ingress player stats: {}".format(player_name))
	plt.plot(stats_date, player_recharged, 'b-')
	plt.xticks(stats_date, color='b', rotation=45)
	plt.ylabel("XM Recharged", color='b')
	plt.xlabel("Time", color='b')
	plt.savefig('images/{}.png'.format(cid))
	img = open('images/{}.png'.format(cid), 'rb')
	log.debug("Before send stats")
	bot.send_photo(cid, img)
	log.debug("After send stats")
	try:
		os.remove('images/{}.png'.format(cid))
	except:
		pass


@bot.message_handler(commands=['test', 'help'])
def send_test(message):
	cid = message.chat.id
	agent_telegram_id = message.from_user.id
	conn = sqlite3.connect('agent_stats.db')
	c = conn.cursor()

	player_recharged = []

	stats_date = []
	for row in c.execute("SELECT * FROM agents_stats WHERE agent_telegram_id={}".format(agent_telegram_id)):
		stats_date.append('{} {}'.format(row[4], row[5]))
		player_recharged.append(row[24])
	conn.close()
	player_name = row[2]

	plt.clf()
	plt.title("Ingress player stats: {}".format(player_name))
	plt.plot(stats_date, player_recharged, 'b-')
	plt.xticks(stats_date, color='b', rotation=45)
	plt.ylabel("XM Recharged", color='b')
	plt.xlabel("Time", color='b', rotation=45)
	plt.tight_layout()

	plt.savefig('images/{}.png'.format(cid))
	img = open('images/{}.png'.format(cid), 'rb')
	log.debug("Before send test")
	bot.send_photo(cid, img)
	log.debug("After send test")
	try:
		os.remove('images/{}.png'.format(cid))
	except:
		pass


@bot.message_handler(commands=['test1', 'help'])
def send_test1(message):
	cid = message.chat.id
	agent_telegram_id = message.from_user.id
	conn = sqlite3.connect('agent_stats.db')
	c = conn.cursor()

	player_ap = []
	player_recharged = []
	player_resonator_deployed = []
	player_links_created = []
	player_control_field_created = []

	stats_date = []
	for row in c.execute("SELECT * FROM agents_stats WHERE agent_telegram_id={}".format(agent_telegram_id)):
		# print(row)   
		# stats_date.append(row[4])
		stats_date.append('{} {}'.format(row[4], row[5]))
		player_ap.append(row[8])
		# player_uniekportal.append(row[9])
		player_resonator_deployed.append(row[17])
		player_links_created.append(row[18])
		player_control_field_created.append(row[19])
		player_recharged.append(row[24])
	conn.close()
	player_name = row[2]

	fig, host = plt.subplots()
	fig.subplots_adjust(right=0.75)

	par1 = host.twinx()
	par2 = host.twinx()

	# Offset the right spine of par2.  The ticks and label have already been
	# placed on the right by twinx above.
	par2.spines["right"].set_position(("axes", 1.2))
	# Having been created by twinx, par2 has its frame off, so the line of its
	# detached spine is invisible.  First, activate the frame but make the patch
	# and spines invisible.
	make_patch_spines_invisible(par2)
	# Second, show the right spine.
	par2.spines["right"].set_visible(True)

	p1, = host.plot(stats_date, player_ap, "b-", label="Player AP")
	p2, = par1.plot(stats_date, player_links_created, "r-", label="Linkes created")
	p3, = par2.plot(stats_date, player_control_field_created, "g-", label="Control field created")

	host.tick_params('x', labelrotation=90)

	par1.set_ylim(0, max(player_links_created))
	par2.set_ylim(0, max(player_control_field_created))

	host.set_xlabel("Time")
	host.set_ylabel("Player AP")
	par1.set_ylabel("Linkes created")
	par2.set_ylabel("Control field created")

	host.yaxis.label.set_color(p1.get_color())
	par1.yaxis.label.set_color(p2.get_color())
	par2.yaxis.label.set_color(p3.get_color())

	tkw = dict(size=4, width=1.5)
	host.tick_params(axis='y', colors=p1.get_color(), **tkw)
	par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
	par2.tick_params(axis='y', colors=p3.get_color(), **tkw)
	host.tick_params(axis='x', **tkw)

	lines = [p1, p2, p3]

	host.legend(lines, [l.get_label() for l in lines])
	plt.tight_layout()
	plt.show()
	plt.savefig('images/{}.png'.format(cid))
	img = open('images/{}.png'.format(cid), 'rb')
	bot.send_photo(cid, img)
	try:
		os.remove('images/{}.png'.format(cid))
	except:
		pass


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	global agent_stats_objects
	cid = message.chat.id
	agent_telegram_id = message.from_user.id
	agent_stats_zip = []
	agent_stats_insert = []
	if message.text.startswith('Time Span'):
		reply = 'Agent stats:\n'
			
		stats_counter = 0
		agent_stats = message.text.split('\n')
		if agent_stats[1].startswith('ALL TIME'):
			agent_stats_values = agent_stats[1].split('ALL TIME ')[1].split(' ')
			agent_stats_values.insert(0,"ALL TIME")

		if agent_stats[1].startswith('ALLE'):
			agent_stats_values = agent_stats[1].split('ALLE ')[1].split(' ')
			agent_stats_values.insert(0,"ALLE")


		for stats in agent_stats_objects:
			if stats in message.text:
				agent_stats_zip.append((stats, agent_stats_values[stats_counter]))
				stats_counter += 1
			else:
				agent_stats_zip.append((stats, 0))

		# agent_stats_zip = zip(agent_stats_objects,agent_stats_values)
		agent_stats_insert = []
		for k,v in agent_stats_zip:
			agent_stats_insert.append(v)
			print(k,v)
			reply += ('{} - {}\n'.format(k,v))

		try:
			log.info("Before reply msg")
			bot.send_message(cid, '{}'.format(reply))
			log.info("After reply msg")
		# bot.send_message(id, text)
		except Exception as e:
			time.sleep(1)
			log.debug("Exeption: {} - Before reply msg".format(e))
			bot.send_message(cid, '{}'.format(reply))
			log.debug("Exeption: {} - After reply msg".format(e))

		agent_stats_insert.insert(0,agent_telegram_id)

		conn = sqlite3.connect('agent_stats.db')
		c = conn.cursor()

		# Insert a row of data		
		c.execute('INSERT INTO agents_stats VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', agent_stats_insert)
		conn.commit()
		conn.close()

try:
	init_db()
except sqlite3.OperationalError:
	pass
#bot.polling()

try: 
    log.debug("Before bot polling")
    bot.polling(none_stop=True)
    log.debug("After bot polling")
except Exception as e:# urllib.error.HTTPError:
    time.sleep(3)
    log.debug("Exeption: {} - Before bot polling".format(e))
    bot.polling(none_stop=True)
    log.debug("Exeption: {} - After bot polling".format(e))

# while True:
#     time.sleep(20)


