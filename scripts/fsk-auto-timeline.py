""" Purpose of this script is to automate protocol creation for Agrobacterium mediated transformation of Fusarium solani strain K
Input: Several parameters that are required to create the protocol, such as number of constructs, antibiotic resistance, 
number of plates per transformation, starting date, are there available competent cells or not
Output: A protocol with days and dates, exported in a txt or doc file for further curation or PDF """

pip install datetime
import datetime

def data_input():
""" Ask for input from the user, to customize protocol """
	# Number of constructs
	construct_number = int(input(f'Number of constructs for transformation (e.g. 5): '))
	if construct_number == 1:
		con_name = str(input(f"Please enter your construct's name: "))
		# agrobacterium antibiotic resistance gene
		agro_antib_name = str(input(f'Antibiotic name used for Agrobacterium: '))
		# agrobacterium antibiotic resistance concentration ug/mL
		agro_antib_conc = int(input(f'Antibiotic concentration used for Agrobacterium: '))	
	elif construct_number > 1:
		print(f"Please enter your constructs' names")
		name_lst = []
		for n in construct_number:
			name = str(input(f'Construct {n}: '))
			con_name_lst = name_lst.append(name)
	else:
		print(f'Please choose valid construct number')
		break

	# Number of plates per construct to calculate plates needed for transfers, 
	plates_per_construct = int(input(f'Number of plates per construct for transformation: '))
	# Construct Names


	# Competent cells available? 
	agro_comp_cells = str(input(f'Are Agrobacterium competent cells available? Answer yes or no : '))
	
	# FsK antibiotic resistance gene for transformation
	fsk_antib_name = str(input(f'Antibiotic name used for FsK selection during transformation: '))
	fsk_antib_name_abbrev = str(input(f'Abbreviation of antibiotic name used for FsK selection during transformation: '))
	# agrobacterium antibiotic resistance concentration ug/mL
	fsk_antib_conc = int(input(f'Antibiotic concentration used for FsK selection during transformation (ug/mL): '))
	# Ask if FsK strain is WT or other
	fsk_strain_wt = str(input(f'Are you using FsK WT (NEK) as parent strain? Answer yes or no: '))
	if fsk_strain_wt == "yes":
		# if WT strain, nothing needs to be asked (no extra/competing antibiotic)
		break
	elif fsk_strain_wt == "no":
		# if other WT strain, then ask the name (for protocol) and specify antibiotic  to see if they compete with current selection
		fsk_strain_other = str(input(f'Name for parent FsK strain used: '))
		fsk_other_antib_name = str(input(f'Antibiotic name used for parent FsK strain selection: '))
		fsk_other_antib_name_abbrev = str(input(f'Abbreviation of antibiotic name used for FsK selection during transformation: '))
		fsk_other_antib_conc = int(input(f'Antibiotic concentration used for parent FsK strain selection (ug/mL): '))
	else:
		print(f'Please asnwer yes or no.')

	#This goes to main calculactions/checks that everything is in order, not data input
	if fsk_antib_name == fsk_other_antib_name or fsk_antib_name_abbrev == fsk_other_antib_name_abbrev:
		print(f'Warning!: Parent strain also has resistance to {fsk_antib_name}. Selection will not be successful.')

	
	
	#TODO: ask for , starting date