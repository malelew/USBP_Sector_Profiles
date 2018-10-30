import pandas as pd

merged_csv = "merged.csv"
handcleaned_csv = "handclean_merged.csv"
southern_sector = ["Big Bend", "Del Rio", "El Centro", "El Paso", "Laredo", "Rio Grande Valley", "San Diego", "Tucson", "Yuma"]

df = pd.read_csv(handcleaned_csv)
col_names = list(df)

df = df[df["SECTOR"].isin(southern_sector)]

staffing_df = df[["SECTOR", "AGENT_STAFFING", "YEAR"]]
apprehensions_df = df[["SECTOR", "APPREHENSIONS", "YEAR"]]
staffing_apprehensions_df = df[["SECTOR", "AGENT_STAFFING", "APPREHENSIONS", "YEAR"]]

staffing_df.to_json("southern_staffing.json", orient="records")
apprehensions_df.to_json("southern_apprehensions.json", orient="records")
staffing_apprehensions_df.to_csv("sothern_staffing_apprehensions.csv", index=False)
df.to_csv("handclean_merged_southern.csv", index=False)
print "done"
