""" Purpose of this script is to automate protocol creation for Agrobacterium mediated transformation of Fusarium solani strain K
Input: Several parameters that are required to create the protocol, such as number of constructs, antibiotic resistance, 
number of plates per transformation, starting date, are there available competent cells or not
Output: A protocol with dates, exported in a txt or doc file for further curation or PDF """

#import

def data_input():
""" Ask for input from the user, to create constructs """
	# Number of constructs
	construct_number = int(input(f'Number of constructs for transformation:'))
	# Number of plates per construct to calculate plates needed for transfers, 
	plates_per_construct = int(input(f'Number of plates per construct for transformation:'))
	# Construct Names
	print(f"Please enter your constructs' names")
	for n in construct_number:
		str(input(f'Construct {n}: '))
	# agrobacterium antibiotic resistance gene
	agro_antib_name = str(input(f'Antibiotic name used for Agrobacterium:'))
	# agrobacterium antibiotic resistance concentration ug/mL
	agro_antib_conc = int(input(f'Antibiotic concentration used for Agrobacterium:'))
	# Competent cells available? 
	agro_comp_cells = str(input(f'Are Agrobacterium competent cells available?'))
	# agrobacterium antibiotic resistance gene
	fsk_antib_name = str(input(f'Antibiotic name used for FsK selection:'))
	# agrobacterium antibiotic resistance concentration ug/mL
	fsk_antib_conc = int(input(f'Antibiotic concentration used for FsK selection (ug/mL):'))
	# Number of constructs
	int(input())
	#TODO: ask for FsK strain, resistance , starting date