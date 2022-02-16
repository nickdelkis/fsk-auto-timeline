""" Purpose of this script is to automate protocol creation for Agrobacterium mediated transformation of Fusarium solani
strain K
Input: Several parameters that are required to create the protocol, such as number of constructs, antibiotic resistance,
number of plates per transformation, starting date, are there available competent cells or not
Output: A protocol with day numbers from starting date and dates, exported in a txt or doc file for further curation
or PDF ready for print. """

import sys
from datetime import datetime, timedelta
from dateutil import parser
from math import ceil
import pandas as pd


class Construct:
    def __init__(self):
        self.name = ""
        self.agro_antib_name = ""
        self.agro_antib_conc = 0
        self.fsk_antib_name = ""
        self.fsk_antib_conc = 0
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
                print(f'Error: Parent strain {self.fsk_other_strain} also has resistance to {self.fsk_antib_name}.')
                sys.exit(1)
        else:
            print(f'Please answer yes or no.')
            sys.exit(1)
        return self.name, self.agro_antib_name, self.agro_antib_conc, self.fsk_antib_name, self.fsk_antib_conc,\
               self.fsk_wt_strain, self.fsk_other_strain, self.fsk_other_antib_name


def data_input():
    """ Ask for input from the user, to customize protocol """
    # Number of constructs
    global construct_number
    construct_number = int(input(f'Number of constructs for transformation (e.g. 5): '))
    if construct_number > 0:
        print(f"Please enter your constructs' names")
        construct_list = []
        global name_list
        name_list = []
        global agro_antib_name_list
        agro_antib_name_list = []
        global agro_antib_conc_list
        agro_antib_conc_list = []
        global fsk_antib_name_list
        fsk_antib_name_list = []
        global fsk_antib_conc_list
        fsk_antib_conc_list = []
        global fsk_wt_strain_list
        fsk_wt_strain_list = []
        global fsk_other_strain_list
        fsk_other_strain_list = []
        global fsk_other_antib_name_list
        fsk_other_antib_name_list = []
        for n in range(construct_number):
            c = f'c{n + 1}'
            construct_list.append(c)
        for c in construct_list:
            c = Construct()
            c.add()
            name_list.append(c.name)
            agro_antib_name_list.append(c.agro_antib_name)
            agro_antib_conc_list.append(c.agro_antib_conc)
            fsk_antib_name_list.append(c.fsk_antib_name)
            fsk_antib_conc_list.append(c.fsk_antib_conc)
            fsk_wt_strain_list.append(c.fsk_wt_strain)
            fsk_other_strain_list.append(c.fsk_other_strain)
            fsk_other_antib_name_list.append(c.fsk_other_antib_name)
    else:
        print(f'Warning! Please choose a valid construct number.')
        sys.exit(1)
    # Number of plates per construct to calculate plates needed for transfers and initial transformations
    global plates_per_construct
    plates_per_construct = int(input(f'Number of plates per construct for transformation (e.g. 5): '))

    # Competent cells available? Will include one week of competent cell preparation if answer is no
    global agro_comp_cells
    agro_comp_cells = str(input(f'Are Agrobacterium competent cells available? Answer yes or no : '))
    if not agro_comp_cells == 'yes' or agro_comp_cells == 'no':
        print(f'Please answer yes or no.')
        sys.exit(1)

    # Ask for starting date (uses dateutil parser so strict format not required)
    global starting_date
    starting_date = parser.parse(input("Enter experiment's starting date: "))
    print(starting_date)


def round_up(n, decimals=-2):
    """Round up numbers for media preparation, when calculating volumes. Default in when doing big volumes, in mL"""
    multiplier = 10 ** decimals
    return ceil(n * multiplier) / multiplier


def calculate():
    """Calculate all required components for performing the protocol.
    This contains plates, membranes, media, media components. Also uses round_up() to make some volumes look better."""
    # Calculate plates per transfer/transformation
    global plate_batch
    plate_batch = construct_number * plates_per_construct + 10
    # CN calculate membranes for transformation
    global membranes
    membranes = construct_number * plates_per_construct + 5
    # calculate IM liquid medium required to go through all necessary steps, plus overage in mL
    global im_ml
    im_ml = round_up(construct_number * 60)
    im_lt = im_ml / 1000

    # calculate volume in microliters for pottasium phosphate 1.25M pH=4.8 - 800 per liter
    global pot_phosph
    pot_phosph = im_lt * 800
    # 50 X MN buffer in mL - 20 per lt
    global mn_buffer
    mn_buffer = im_lt * 20
    # 1000X IM salts in mL - 5 per lt
    global im_salts
    im_salts = im_lt * 5
    # MES 1M pH 5.6 - 40 per lt
    global mes
    mes = im_lt * 40
    # CaCl - 0.02 g per lt
    global cacl
    cacl = im_lt * 0.02
    # FeSO4 1mg/mL - 1 mL per lt
    global feso4
    feso4 = im_lt
    # NH4NO3 - 0.4 g per lt
    global nh4no3
    nh4no3 = im_lt * 0.4
    # glycerol 100% in mL
    global glycerol
    glycerol = im_lt * 5
    # glucose in grams - 1 per lt
    global glucose
    glucose = im_lt
    # agar in grams = 15 g per lt
    global agar
    agar = im_lt * 15
    # acetosyringone 200 mM stock in mL - 1 per liter
    acs = im_lt
    # create recipe list
    global im_buffer_list
    im_buffer_list = [pot_phosph, mn_buffer, im_salts, mes, cacl, feso4, nh4no3, glycerol, glucose]
    # create list with names
    global im_buffer_name_list
    im_buffer_name_list = ["1.25M Potassium Phosphate buffer (μL)", "50X MN buffer (mL)", "1000X IM salts (mL)",
                       "1M MES pH 5.6 (mL)", "CaCl dihydrate (gr)", "1mg/mL FeSO4 (mL)", "NH4NO3 (gr)",
                       "100% Glycerol (mL)", "Glucose (gr)"]
    return plate_batch, membranes, im_lt


def create_table():
    """Create table with strains, antibiotics, plates per construct
    Use pandas and dataframe function"""
    construct_table_dict = {"Construct Name": name_list, "Agrobacterium Antibiotic": agro_antib_name_list,
                  "Concentration (ug/mL)": agro_antib_conc_list,
                  "FsK antibiotic": fsk_antib_name_list,
                  "Concentration (ug/mL)": fsk_antib_conc_list,
                  "FsK WT strain as parent": fsk_wt_strain_list,
                  "FsK parent strain name": fsk_other_strain_list,
                  "FsK parent strain antibiotic": fsk_other_antib_name_list}
    global construct_table
    construct_table = pd.DataFrame(construct_table_dict, index=False)
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    print(construct_table)

    im_buffer_table_dict = {"Component": im_buffer_name_list, "Quantity": im_buffer_list}
    global im_buffer_table
    im_buffer_table = pd.DataFrame(im_buffer_table_dict, index=False)
    print()

    return construct_table


def add_week0():
    # To be used for adding Week 0 (Competent cell preparation) in final protocol
    if agro_comp_cells == 'yes':
        pass
    elif agro_comp_cells == 'no':
        pass  # TODO: Make protocol create a Week 0 for competent cell prep


data_input()
calculate()
create_table()
