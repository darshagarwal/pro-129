import pandas as pd
import csv

df = pd.read_csv("D:\coding\pro-129\dwarf_stars.csv")
#print("df:",df)

#drop all rows that have any NaN values
df = df.dropna()
#print(float(df["Mass"])*0.000954588)

df['Mass']=df['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
df["Mass"] = df["Mass"]*0.000954588

#print(df)

df['Radius'] = df["Radius"]*0.102763

headers = df[0]
dwaf_stars_data = df[1:]

with open("DataMerging.csv","w") as f:
        csv_write = csv.writer(f)
        csv_write.writerow(headers)
        csv_write.writerows(dwaf_stars_data)

star_df = pd.read_csv("D:\coding\pro-129\bright_stars.csv")

headers_star = star_df[0]
brightest_star = star_df[1:]

data_mersing_headers=[headers_star+headers]

data_mersing = [brightest_star+dwaf_stars_data]

with open("Final_Data_Mersing.csv","w") as f:
    csv_write = csv.writer(f)
    csv_write.writerow(data_mersing_headers)
    csv_write.writerows(data_mersing)