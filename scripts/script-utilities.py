""" Purpose of this script is to automate protocol creation for Agrobacterium mediated transformation of Fusarium solani
strain K
Input: Several parameters that are required to create the protocol, such as number of constructs, antibiotic resistance,
number of plates per transformation, starting date, are there available competent cells or not
Output: A protocol with day numbers from starting date and dates, exported in a txt or doc file for further curation
or PDF ready for print. """

import sys
from datetime import datetime, timedelta
from dateutil import parser
from tabulate import tabulate


class Construct:
    def __init__(self):
        self.name = ""
        self.agro_antib_name = ""
        self.agro_antib_conc = ""
        self.fsk_antib_name = ""
        self.fsk_antib_conc = ""
        self.fsk_wt_strain = ""
        self.fsk_other_strain = ""
        self.fsk_other_antib_name = ""

    def add(self):
        # Construct x Name
        self.name = str(input(
            f'Construct name: '))
        # agrobacterium antibiotic resistance
        self.agro_antib_name = str(input(
            f'Antibiotic used for selection of Agrobacterium strain containing {self.name}: '))
        # agrobacterium antibiotic resistance concentration ug/mL
        self.agro_antib_conc = int(input(
            f'Antibiotic concentration used for selection of Agrobacterium strain containing {self.name} (ug/mL): '))
        # FsK antibiotic resistance gene for transformation
        self.fsk_antib_name = str(input(
            f'Antibiotic name used for FsK selection during transformation: '))
        # fsk antibiotic resistance concentration ug/mL
        self.fsk_antib_conc = int(input(
            f'Antibiotic concentration used for FsK selection during transformation (ug/mL): '))
        # Ask if fsk strain is WT or not
        self.fsk_wt_strain = str(input(f'Are you using FsK WT (NEK) as parent strain? Answer yes or no: '))
        if self.fsk_wt_strain == "yes":
            # if WT strain, nothing needs to be asked (no extra/competing antibiotic)
            pass
        # if uses other fsk strain,
        elif self.fsk_wt_strain == "no":
            # if other WT strain, then ask the name (for protocol) and specify antibiotic
            # to see if they compete with current selection
            self.fsk_other_strain = str(input(f'Name for parent FsK strain used: '))
            fsk_other_antib_name = str(input(f'Antibiotic name used for parent FsK strain selection: '))
            if self.fsk_antib_name == fsk_other_antib_name:
                print(f'Warning!: Parent strain {self.fsk_other_strain} also has resistance to {self.fsk_antib_name}.')
                sys.exit(1)
        else:
            print(f'Please answer yes or no.')
            sys.exit(1)


def data_input():
    """ Ask for input from the user, to customize protocol """
    # Number of constructs
    construct_number = int(input(f'Number of constructs for transformation (e.g. 5): '))
    if construct_number > 0:
        print(f"Please enter your constructs' names")
        construct_list = []
        for n in range(construct_number):
            c = f'c{n+1}'
            construct_list.append(c)
            print(construct_list)
        for c in construct_list:
            c = Construct()
            c.add()
    else:
        print(f'Warning! Please choose a valid construct number.')
        sys.exit(1)

    # Number of plates per construct to calculate plates needed for transfers and initial transformations
    plates_per_construct = int(input(f'Number of plates per construct for transformation (e.g. 5): '))
    # Calculate plates and membranes needed per transfer/transformation
    global plate_batch
    plate_batch = construct_number * plates_per_construct + 10
    global membranes
    membranes = construct_number * plates_per_construct + 5

    # Competent cells available? Will include one week of competent cell preparation if answer is no
    agro_comp_cells = str(input(f'Are Agrobacterium competent cells available? Answer yes or no : '))
    if agro_comp_cells == 'yes':
        pass
    else:
        print(f'Please answer yes or no.')
        sys.exit(1)

    # Ask for starting date (uses dateutil parser so strict format not required)
    starting_date = parser.parse(input("Enter experiment's starting date: "))
    print(starting_date)


def create_table():
    """Create table with strains, antibiotics, plates per construct"""


data_input()
print(plate_batch)
print(membranes)
