import pandas as pd
from os import listdir

curr_dir = "."
csv_suffix = ".csv"
psheets_dir = "../sheets/camelot_scrape/"
col_names = ['SECTOR', 'AGENT_STAFFING', 'APPREHENSIONS', 'OTHER_THAN_MEXICAN_APPREHENSIONS', 'CANNABIS', 'COCAINE', 'ACCEPTED_PROSECUTIONS', 'ASSAULTS', 'RESCUES', 'DEATHS']

# get the pdf file names
csv_files = [f for f in listdir(curr_dir) if f.endswith(csv_suffix)]

for sheet in csv_files:
    curr_df = pd.read_csv(sheet, names=col_names)
    curr_df = curr_df.dropna(subset=[col_names[0], col_names[1]])
    curr_df.to_csv(psheets_dir + sheet, index=False)

print "done"
