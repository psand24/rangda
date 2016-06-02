#here goes nothing

from sys import exit

import story

turn_count = 0
villager_total = 120
villagers_lost = 6 * turn_count
villagers_saved = villager_total - villagers_lost
weight = 0
age = 0
sex = 0
men = 1
women = 2
both = 3
pansexual = 4
inanimate_objects = 5


barong_artifact = 0
dukun_artifact = 0

def pre_start():
	print "Please enter your age:"
	global age	
	age = raw_input("> ")
	print "Please enter your weight in lbs:"
	global weight
	weight = raw_input("> ")
	print """Please enter your romantic preference:
			*interested in MEN
			*interested in WOMEN
			*interested in BOTH
			*PANSEXUAL
			*interested in inanimate OBJECTS
			"""
	while True:
		global sex, men, women, both, pansexual, objects
		choice = raw_input("> ").upper()
		if "men" in choice:
			sex += 1
			start()
		elif "women" in choice:
			sex += 2
			start()
		elif "both" in choice:
			sex += 3
			start()
		elif "pansexual" in choice:
			sex += 4
			start()
		elif "objects" in choice:
			sex += 5
			start()
		else:
			print story.entryerror
	


def start():
	print story.start
	while True:
		choice = raw_input("> ").upper()
		
		if "DUKUN" in choice:
			dukun()
		elif "RANKS" in choice:
			ranks()
		elif "BARONG" in choice:
			barong()
		elif "STABBING" in choice:
			stabbing()
		elif "FLEE" in choice:
			print story.flee
			exit()
		#for debuging below
		elif "INSTANT WIN" in choice:
			global barong_artifact
			global dukun_artifact
			barong_artifact = 1
			dukun_artifact = 1
			confront()
		else:
			print story.entryerror


def stabbing():
	print story.stabbing
	global turn_count
	turn_count += 1
	dead()


def ranks():
	global turn_count
	turn_count += 1
	print story.ranks
	raw_input(" ")
	print story.ranks_2
	
	while True:
		turn_count += 1
		choice = raw_input("> ").upper()
		if "STABBING" in choice:
			print story.stabbing_2_electric_boogaloo
			raw_input(" ")
			print story.stabbing_2_2
			dead()
		elif "FALCON STRIKE" in choice:
			print story.falcon_strike
			raw_input("> ")
			print story.falcon_strike2
			raw_input("> ")
			print story.falcon_strike3
			raw_input("> ")
			dead_to_me()
		else:
			print story.entryerror



def barong():
	print story.barong
	global turn_count
	turn_count += 1
	
	while True:
	
		choice = raw_input("> ").upper()
		
		if "BUTTPART" in choice:
			buttpart()
		elif "WARUNG" in choice:
			warung()
		elif "BACK" in choice:
			turn_count += 1
			odalan_x()
		else:
			print story.entryerror
	

def buttpart():
	global turn_count
	turn_count += 1
	print story.buttpart
	raw_input("> ")
	print story.buttpart_2
	raw_input("> ")
	print story.buttpart_3
	raw_input("> ")
	print story.buttpart_4
	raw_input("> ")
	global villager_total
	villager_total = 60
	dead_half()
	
	

def warung():
	print story.warung1
	raw_input(" ")
	print story.warung2
	global turn_count
	turn_count += 1
	while True:
		choice = raw_input(" > ").upper()
		if "PHONE" in choice:
			turn_count += 1
			print story.phone
			dead()
		elif "RUPEES" in choice:
			print story.rupees
			turn_count += 2
			while True:
				choice = raw_input("> ").upper()
				if "RUBLES" in choice:
					rubles()
				elif "PHONE" in choice:
					turn_count += 1
					print story.phone
					dead()
				elif "BACK" in choice:
					odalan_x()
				else:
					print story.entryerror
		elif "RUBLES" in choice:
			rubles()
		else:
			print story.entryerror
			
	
def rubles():	
	print story.rubles
	
			
	global turn_count
	turn_count += 1
	global barong_artifact
	barong_artifact = 1
	while True:
		
		choice = raw_input(" >").upper()
		
		if "BACK" in choice: 
			odalan_x()
		elif "STAY" in choice:
			print story.stay
			turn_count += 1
			dead()
		else:
			print story.entryerror
	

def dukun():
	print story.dukun
	
	global turn_count
	turn_count += 1
	
	while True:
		
		choice = raw_input(" >").upper()
		
		if "BACK" in choice:
			odalan_x()
		
		elif "BYSTANDER" in choice:
			bystander()
			
		elif "CROWDSURF" in choice:
			crowdsurf()
		else:
			print story.entryerror
			
	
def bystander():
	global turn_count
	turn_count += 1
	
	print story.bystander
	raw_input(" ")
	print story.bystander2
	
	while True:
		choice = raw_input("> ").upper()
		if "EAT PRAY LOVE" in choice:
			casual()
		elif "HOPE FLOATS" in choice or "MISS CONGENIALITY" in choice:
			rage()
		elif "ERIN BROKOVICH" in choice or "PRETTY WOMAN" in choice or "MYSTIC PIZZA" in choice:
			print story.discussion
			turn_count += 1
			dead()
		elif "MY BEST FRIEND'S WEDDING" in choice:
			throw()
		else:
			print story.entryerror

def casual():
	global turn_count
	turn_count += 1
	print story.casual
	while True:
		choice = raw_input("> ").upper()
		if "BACK" in choice:
			odalan_x()
		if "CROWDSURF" in choice:
			crowdsurf()
		else:
			print story.entryerror

def rage():
	global turn_count
	turn_count += 1
	print story.rage
	dead()
	
def throw():
	global turn_count
	turn_count += 1
	print story.throw
	raw_input("> ")
	bale()
	

def crowdsurf():
	global turn_count
	turn_count += 1
	print story.crowdsurf
	raw_input("> ")
	print story.crowdsurf_2A
	dead()
	# EVENTUALLY A WEIGHT CHECK WILL BE HERE, ALLOWING A VERY SMALL PERSON TO MOVE FORWARD TO THE BALE
	# BY CROWDSURFING SUCCESSFULLY (story.crowdsurf_2B), BUT LOSING 3 TURNS

def bale():
	global turn_count
	turn_count += 1
	print story.bale
	while True:
		choice = raw_input("> ").upper()
		if "SALAK" in choice:
			print story.salak
			raw_input("> ")
			print story.salak_b
			dead()
		elif "CELEBRITY" in choice:
			print story.kimmy
			raw_input("> ")
			print story.kimmy2
			global dukun_artifact
			dukun_artifact = 1
			raw_input("> ")
			odalan_x()

def odalan_x():
	global turn_count
	turn_count += 1
	if barong_artifact == 0 and dukun_artifact == 0:
		odalan_nothing()
	elif barong_artifact == 1 and dukun_artifact == 1:
		odalan_both()
	elif barong_artifact == 1 and dukun_artifact == 0:
		odalan_barong_only()
	elif barong_artifact == 0 and dukun_artifact == 1:
		odalan_dukun_only()
	else:
		print "i don't know why this happened ERROR"
		exit()
	
	
def odalan_nothing():
	print story.odalan_nothing
	while True:
		choice = raw_input("> ").upper()
		
		if "DUKUN" in choice:
			dukun()
		elif "RANKS" in choice:
			ranks()
		elif "BARONG" in choice:
			barong()
		elif "STABBING" in choice:
			stabbing()
		elif "FLEE" in choice:
			global turn_count
			turn_count += 1
			print story.flee
			exit()
		else:
			print story.entryerror
			
def odalan_both():
	print story.odalan_both
	while True:
		choice = raw_input("> ").upper()
		
		if "CONFRONT" in choice:
			confront()
		elif "STABBING" in choice:
			stabbing()
		elif "FLEE" in choice:
			global turn_count
			turn_count += 1	
			print story.flee
			exit()
		else:
			print story.entryerror
	
	
def odalan_barong_only():
	print story.odalan_barong_only
	while True:
		choice = raw_input("> ").upper()
		
		if "DUKUN" in choice:
			dukun()
		elif "CONFRONT" in choice:
			confront()
		elif "STABBING" in choice:
			stabbing()
		elif "FLEE" in choice:
			global turn_count
			turn_count += 1	
			print story.flee
			exit()
		else:
			print story.entryerror
	
def odalan_dukun_only():
	print story.odalan_dukun_only
	while True:
		choice = raw_input("> ").upper()
		
		if "BARONG" in choice:
			barong()
		elif "CONFRONT" in choice:
			confront()
		elif "STABBING" in choice:
			stabbing()
		elif "FLEE" in choice:
			global turn_count
			turn_count += 1
			print story.flee
			exit()
		else:
			print story.entryerror

def confront():
	global turn_count
	turn_count += 1
	if barong_artifact == 0 and dukun_artifact == 0:
		print story.confront_nothing
		raw_input("> ")
		print story.confront_nothing2
		raw_input("> ")
		dead()
	elif barong_artifact == 1 and dukun_artifact == 1:
		print story.confront_both
		raw_input("> ")
		print story.confront_both2
		print '\t\t\t\tturns taken: %d' % turn_count
		print story.confront_both3
		raw_input("> ")
		exit()
	elif barong_artifact == 1 and dukun_artifact == 0:
		print story.confront_barong_only
		raw_input("> ")
		print story.confront_barong_only2
		raw_input("> ")
		dead()
	elif barong_artifact == 0 and dukun_artifact == 1:
		print story.confront_dukun_only
		raw_input("> ")
		print story.confront_dukun_only2
		raw_input("> ")
		dead()
	else:
		print "i don't know why this happened ERROR"
		exit()
	
def dead():
	global turn_count
	global villagers_saved
	villagers_saved = 0
	print '\n\t\t\t\t\tYOU DEAD'
	print '\n\t\t\t\t\tturns taken: %d\n' % turn_count
	print '\t\t\t\t\tvillagers saved: %s\n\n' % villagers_saved
	exit()

def dead_half():
	global turn_count
	global villagers_saved
	villagers_saved = 60
	print '\n\t\t\t\t\tYOU DEAD'
	print '\n\t\t\t\t\tturns taken: %d\n' % turn_count
	print '\t\t\t\t\tvillagers saved: %s\n\n' % villagers_saved
	exit()

def dead_to_me():
	global turn_count
	global villagers_saved
	villagers_saved = 120
	print '\n\t\t\t\t\tYOU\'RE DEAD (to me)'
	print '\n\t\t\t\t\tturns taken: %d\n' % turn_count
	print '\t\t\t\t\tvillagers saved: %s\n\n' % villagers_saved
	exit()

start()