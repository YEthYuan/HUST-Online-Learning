import os
import pandas as pd


path = "../"
len_thres = 10000
num = 9


fl = []
counter = 0
df_out = pd.DataFrame()
for file in os.listdir(path):
    if ".csv" in file:
        fl.append(file)

# print(fl)

for file in fl:
    fname = file[:-4]
    fpath = path+file
    df = pd.read_csv(fpath)
    # print(fname)
    # print(df.head())
    fdata = df['High']

    if len(fdata)>len_thres:
        fdata = fdata[:len_thres]
        df_out[fname] = fdata

print(df_out)
df_out.to_csv('data.csv', index=False)