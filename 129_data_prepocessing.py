import pandas as pd

stars_data_file = pd.read_csv("brown_dwarfs_data.csv")

new_stars_datafile = stars_data_file.dropna()

new_stars_datafile["Star_name"] = new_stars_datafile["Star_name"].astype(str)
new_stars_datafile["Radius"] = (new_stars_datafile["Radius"].astype(float))
new_stars_datafile["Mass"] = (new_stars_datafile["Mass"].astype(float))

new_stars_datafile["Radius"] = (new_stars_datafile["Radius"]*0.102763)
new_stars_datafile["Mass"] = (new_stars_datafile["Mass"]*0.000954588)

headers = ['Star_name','Distance','Mass','Radius']
new_stars_data_file = pd.DataFrame(new_stars_datafile, columns=headers)
new_stars_data_file.to_csv('new_dwarf_stars_data.csv', index=False)

dwarf_stars = pd.read_csv("new_dwarf_stars_data.csv")
dwarf_stars.to_csv('new_dwarf_stars_data.csv', index=True, index_label="id")

brown_dwarfs = pd.read_csv("new_dwarf_stars_data.csv")
bright_stars = pd.read_csv("bright_stars_data.csv")


stars_merged_file = pd.merge(brown_dwarfs, bright_stars, on="id")
print(stars_merged_file)
stars_merged_file.to_csv("final_merged_stars.csv")