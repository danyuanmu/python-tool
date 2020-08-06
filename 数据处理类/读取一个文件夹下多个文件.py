import glob
import pandas as pd

path = '' # use your path
def read_path(path):
    all_files = glob.glob(path +"/*.csv")

    li = []

    for filename in all_files:
        df = pd.read_csv(filename,engine='python',encoding="gb2312")
        li.append(df)
    data = pd.concat(li, axis=0, ignore_index=True)
    return data