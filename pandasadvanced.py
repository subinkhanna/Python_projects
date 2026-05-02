import pandas as pd

#df = pd.DataFrame([[1],[2],[3]], columns=['a'], index=[1,2,3])

df = pd.DataFrame([[1,0,9],[2,1,3],[3,4,3]], columns=['a','b','c'], index=[1,2,3])

#print(df.columns.to_list())
#print(df.index.to_list())

#print(df.describe())

#print(df.nunique())
#print(df['b'].nunique())
#print(df.shape)
#print(df.info())

coffee = pd.read_csv("C:\\Python_projects\\coffee.csv")
#print(coffee.head(2))
#print(coffee.tail(2))

#result = pd.read_feather("C:\\Python_projects\\results.feather")
#print(result.head(2))


result = pd.read_parquet("C:\\Python_projects\\results.parquet")
#print(result.head(2))

#print(coffee.sample(3))
#print(result.sample(2))

#print(coffee.sample(1, random_state=1))

#print(coffee.loc[1:8, ["Units Sold", "Day"]])

#print(coffee.iloc[1:8])    ##iat & at can be used to access specific value more efficiently - can't be used for ranges

##print(coffee.sort_values(["Day", "Units Sold"], ascending=[True, False]))

##for index, row in coffee.iterrows():
##    print(index, row)

bios = pd.read_csv("C:\\Python_projects\\bios.csv")

#print(bios.head())

#print(bios[bios["height_cm"] > 215])

#print(bios.loc[bios["height_cm"] > 215, ["name","height_cm"]])


#print(bios[(bios["height_cm"] > 215) & (bios["born_country"] == 'USA')].head())


#print(bios[(bios["name"].str.contains("keith", case=False) )].head())
#print(bios[(bios["name"].str.contains("keith") )].head())   <-- Case sensitive

#print(bios[(bios["name"].str.contains("keith|patrick", case=False) )].head())   ## | (OR)  Keith or Patrick


#print(bios[(bios["born_country"].isin(['USA', 'England']) &  bios["name"].str.contains("keith", case=False))].head())   ## isin operator

#print(bios[(bios["born_country"].isin(['USA', 'England']) &  bios["name"].str.startswith("keith"))].head())


#print(bios[(bios["born_country"].isin(['USA', 'England']) &  bios["name"].str.startswith("keith"))].head())

##Adding a new column

coffee['Price'] = 4.99  
import numpy as np
coffee['New Price'] = np.where(coffee['Coffee Type'] == 'Espresso', 6.99, 4.99)
#print(coffee.head())
coffee.drop(columns=['Price'], inplace=True)
print(coffee.head())

coffee_new = coffee ##coffee_new is pointing to same memory as coffee.
#coffee_new = coffee.copy() ## This makes entirely new copy
#print(coffee_new.head())
#coffee['Price'] = 4.99
#print(coffee.head())
#print(coffee_new.head())

#coffee['Revenue'] = coffee['Units Sold'] * coffee['New Price']
#coffee.rename(columns={'New Price':'Price'}, inplace=True)

#print(coffee.head())

#bios['first_name'] = bios['name'].str.split(' ').str[0]
#print(bios.head())

#bios['born_dtime'] = pd.to_datetime(bios['born_date'])
#bios['born_year'] = bios['born_dtime'].dt.year
#print(bios.head())
#print(bios.info())

bios['height_category'] = bios['height_cm'].apply(lambda x : 'Tall' if x > 215 else 'Average' if x > 160 else 'Short')  ## Can define custom functions

#print(bios.head())

## def custom_function()       bios['col'].apply(custom_function, axis=)    axis=1 is rows, axis=0 is cols

noc = pd.read_csv("C:\\Python_projects\\noc_regions.csv")
#print(noc.head(3))

#bios_updated = pd.merge(bios, noc, left_on="born_country", right_on="NOC", how="left", suffixes=["NOC_bios", "NOC_noc"])
#print(bios_updated.head(3))

#bios_updated.rename(columns={"region":"born_country_full"}, inplace=True)
#print(bios_updated.head(3))


#coffee.loc[[2,3],["Units Sold"]] = np.nan   ##Assigning NaN values using numpy

#print(coffee["Units Sold"].isna())
#print(coffee[coffee["Units Sold"].isna()])
#print(coffee[coffee["Units Sold"].notna()])

#coffee.fillna(value=coffee["Units Sold"].mean(), inplace=True)  ##value=0 or mean of value or interpolate()
#print(coffee.head())

#print(coffee.dropna(subset=["Units Sold"]))    <<to drop NA focusing on subset - column name(s)

##value_counts

#print(bios["born_city"].value_counts())

##print(bios[bios["born_country"]=="USA"]["born_city"].value_counts())

#print(coffee.fillna(value=coffee["Units Sold"].mean(), inplace=True))
#print(coffee.head(5))

#print(coffee.groupby(["Coffee Type"])["Units Sold"].sum())
#print(coffee.groupby(["Coffee Type"])["Units Sold"].mean())
#print(coffee.groupby(["Coffee Type"])["New Price"].mean())
#print(coffee.groupby(["Coffee Type", "Day"]).agg({"Units Sold":"sum","New Price":"mean"}))

#pivot = coffee.pivot(columns="Coffee Type", index="Day", values="Units Sold")
#print(pivot)

#bios['born_dtime'] = pd.to_datetime(bios['born_date'])
#print(bios.groupby(bios["born_dtime"].dt.year)["name"].count().reset_index().sort_values("name", ascending=False))

coffee["revenue"] = coffee["Units Sold"] * coffee["New Price"]

coffee["yesterday_revenue"] = coffee["revenue"].shift(2)

coffee["pct"] = (coffee["revenue"] - coffee["yesterday_revenue"]) / coffee["yesterday_revenue"]

#print(coffee)

##.rank(), .cumsum(), .rolling()

#print(bios['height_cm'].rank(method='average', ascending=False, na_option='bottom'))    ##Rank function

#bios["rank_height_cm"] = bios['height_cm'].rank(method='average', ascending=False, na_option='bottom')

#print(bios.sort_values("rank_height_cm", ascending=True).head(10))

#print(coffee.select_dtypes('Int64').cumsum())
#print(coffee.cumsum(numeric_only=True))

#print(coffee[coffee['Coffee Type']=="Latte"].select_dtypes(["int64","float64"]).rolling(window=3).mean())   ##.mean(), .sum(), .std()