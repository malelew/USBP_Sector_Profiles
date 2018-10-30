import pandas as pd
from os import listdir
import re

curr_dir = "."
sheets_dir = "../"
csv_suffix = ".csv"
new_csv_file = "merged.csv"
# includes a 'YEAR' columm
col_names = ['SECTOR', 'AGENT_STAFFING', 'APPREHENSIONS', 'OTHER_THAN_MEXICAN_APPREHENSIONS', 'CANNABIS', 'COCAINE', 'ACCEPTED_PROSECUTIONS', 'ASSAULTS', 'RESCUES', 'DEATHS', 'YEAR']

# get the pdf file names
csv_files = [f for f in listdir(curr_dir) if f.endswith(csv_suffix)]

new_df = pd.DataFrame(columns=col_names)

for file in csv_files:
    curr_year = re.search(r"(\d{4})", file).group(1)
    df = pd.read_csv(file)
    df[col_names[-1]] = curr_year
    new_df = pd.concat([df, new_df])

new_df = new_df.sort_values(by=col_names[-1])
new_df.to_csv(sheets_dir + new_csv_file, index=False)
print "done"
# df = df[df[col_names[:2]]] # retain only 'SECTOR', 'AGENT_STAFFING', 'APPREHENSIONS'
