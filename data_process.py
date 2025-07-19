import pandas as pd

# Load the Excel
df = pd.read_excel("gw_levels.xlsx")


def extract_avg_depth(value):
    try:
        parts = value.split(" ")[0:3] 
        depth1 = float(parts[0])
        depth2 = float(parts[2])
        return round((depth1 + depth2) / 2, 2)
    except:
        return None

df['avg_depth'] = df['Water Level'].apply(extract_avg_depth)


df = df.dropna(subset=['avg_depth'])


df['Year'] = df['Year'].str.extract(r'(\d{4})').astype(int)


df.to_csv("cleaned_groundwater.csv", index=False)
