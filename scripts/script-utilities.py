""" Purpose of this script is to automate protocol creation for Agrobacterium mediated transformation of Fusarium solani
strain K
Input: Several parameters that are required to create the protocol, such as number of constructs, antibiotic resistance,
number of plates per transformation, starting date, are there available competent cells or not
Output: A protocol with day numbers from starting date and dates, exported in a txt or doc file for further curation
or PDF ready for print. """

import sys
from datetime import datetime, timedelta
from dateutil import parser


def data_input():
	""" Ask for input from the user, to customize protocol """
	# Number of constructs
	construct_number = int(input(f'Number of constructs for transformation (e.g. 5): '))
	if construct_number > 0:
		print(f"Please enter your constructs' names")
		# create empty lists and dicts
		con_name_lst = []
		agro_antib_lst = []
		agro_antib_conc_lst = []
		agro_antib_name_conc_dict = {}
		con_agro_antib_dict = {}
		con_fsk_antib_dict = {}
		fsk_antib_name_conc_dict = {}
		# iterate as many times as constructs to ask name, antibiotic and concentration
		# for selection and add the information to lists and dicts
		for n in range(construct_number):
			# Construct x Name
			name = str(input(f'Construct {n+1} name: '))
			# append name to list of construct names
			con_name_lst.append(name)
			# agrobacterium antibiotic resistance
			agro_antib_name = str(input(f'Antibiotic used for selection of Agrobacterium strain containing {name}: '))
			# append antibiotic name to list of antibiotic names
			agro_antib_lst.append(agro_antib_name)
			# agrobacterium antibiotic resistance concentration ug/mL
			agro_antib_conc = int(input(
				f'Antibiotic concentration used for selection of Agrobacterium strain containing {name} (ug/mL): '))
			# append antibiotic concentration to list of antibiotic concentrations
			agro_antib_conc_lst.append(agro_antib_conc)
			# pair construct name with agro antibiotic and antibiotic with concentration
			con_agro_antib_dict.update({name: agro_antib_name})
			agro_antib_name_conc_dict.update({agro_antib_name: agro_antib_conc})
			# FsK antibiotic resistance gene for transformation
			fsk_antib_name = str(input(f'Antibiotic name used for FsK selection during transformation: '))
			# fsk antibiotic resistance concentration ug/mL
			fsk_antib_conc = int(input(
				f'Antibiotic concentration used for FsK selection during transformation (ug/mL): '))
			# pair construct name fsk antibiotic and antibiotic with concentration
			con_fsk_antib_dict.update({name: fsk_antib_name})
			fsk_antib_name_conc_dict.update({fsk_antib_name: fsk_antib_conc})
	else:
		print(f'Warning! Please choose a valid construct number.')
		sys.exit(1)

	# Number of plates per construct to calculate plates needed for transfers and initial transformations
	plates_per_construct = int(input(f'Number of plates per construct for transformation: '))

	# Competent cells available? Will include one week of competent cell preparation if answer is no
	agro_comp_cells = str(input(f'Are Agrobacterium competent cells available? Answer yes or no : '))

	# Ask if FsK strain is WT or other
	fsk_strain_wt = str(input(f'Are you using FsK WT (NEK) as parent strain? Answer yes or no: '))
	if fsk_strain_wt == "yes":
		# if WT strain, nothing needs to be asked (no extra/competing antibiotic)
		pass
	elif fsk_strain_wt == "no":
		# if other WT strain, then ask the name (for protocol) and specify antibiotic
		# to see if they compete with current selection
		fsk_other_strain = str(input(f'Name for parent FsK strain used: '))
		fsk_other_antib_name = str(input(f'Antibiotic name used for parent FsK strain selection: '))
		if fsk_antib_name == fsk_other_antib_name:
			print(f'Warning!: Parent strain {fsk_other_strain} also has resistance to {fsk_antib_name}.')
			sys.exit(1)
	else:
		print(f'Please answer yes or no.')
		sys.exit(1)
	# Ask for starting date (uses dateutil parser so strict format not required)
	starting_date = parser.parse(input("Enter experiment's starting date: "))
	print(starting_date)


def calculate_variables():
	"""Use data input to calculate all desired variables, like plates for transformation, dates, etc. membranes"""


def create_table():
	"""Create table with strains, antibiotics, plates per construct"""