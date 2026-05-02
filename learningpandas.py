import pandas as pd

#    data = [100.00, 101.09, 110.44, 105.25]
#    labels = ["a","b","c","d"]
#    print(pd.Series(data, index=labels))

#    data = ["apple", "banana", "cat", "doggy"]
#    labels = ["a","b","c","d"]
#    print(pd.Series(data, index=labels))


#    data = [True, False, True, False]
#    labels = ["a","b","c","d"]
#    print(pd.Series(data, index=labels))

#print(pd.Series(data, index=labels).loc["a"])

#    itemlist = {"a": 1.5, "b": 72, "c":200}
#    pdSeries = pd.Series(itemlist)
#    print(pdSeries)

#    print(pdSeries.loc["a"])
#    print(pdSeries[pdSeries > 70])
#    print(pdSeries > 70)

#itemlist = {"a": [1.5], "b": [72], "c":[200]}
#df = pd.DataFrame(itemlist)
#print(df)


itemlist = {"a": 1.5, "b": 72, "c":200}
df = pd.DataFrame(itemlist, index=[0])
print(df)

df["d"] = 150   ## number of values should be equal to number of rows
print(df)

itemlist = {"a": 3.5, "b": 4.72, "c":210, "d":140}
df2 = pd.DataFrame(itemlist, index=[0])
print(df2)

df = pd.concat([df, df2])
print(df)

#print(df.loc[0])

##reading from csv.
#df = pd.read_csv("path_of_csv_file")

##reading from json.
#df = pd.read_json("path_of_json_file")

## to print all rows and columns and not truncated version - use -  to_string()  print(df.to_string())


#selection of columns data from pandas
# selection of column
#print(df["columnname"])
#print(df[["column1", "column2", "column3"]]) ## list of columns for multiple columns

#Selection of rows from pandas using loc, iloc

print(df.loc["index label"])

#column can be projected as index during read_csv
# pd.read_csv("csv file path", index_col=[column name(s)])


#df.loc[<to select rows>, [<to select columns]]
# <to select rows> start:end <- end is inclusive
# columns are entered in list


##integer based selection
# df.iloc[<for rows>,<for colums>]
# df.iloc[start:end:step, start:end:step]

## Aggregate functions


##without numeric_only, these would tend to apply to whole df 
#print(df.mean(numeric_only=True))
#print(df.sum(numeric_only=True))
#print(df.min(numeric_only=True))
#print(df.max(numeric_only=True))
#print(df.std(numeric_only=True))
#print(df.count())
#print(df.var(numeric_only=True))

##group by function

#group = df.groupby("Name of column to be group by")

#group["height"].mean() or group["heigh"].sum()

##.min(), max(), count(0)

## data cleaning-- 

## df.drop(columns=[<<list of columns>>]) 

##df.drop(columns=[col1, col2])

##missing type

##df.dropna(subset=[<<list of columns])  ### list of columns scanned for missing values and are dropped if value is missing

## df.dropna(subset=[col1])

##fill missing value

##df.fillna({"col1":"None"})  ##Fill not available value  fillna takes dictionary of column and value that needs to be filled

##fix inconsistent values

##df["col1"] = df["col1"].replace({"grass":"GRASS"})  ## .replace takes dictionary of original & new value.  More than one key:value pair can be passed


##Standardize text

##df["name"] = df["name"].str.lower()  -- Change to lower. Use string functions with str obj

#df["name"] = df["name"].astype(bool)  -- Change data type of a column

## Remove duplicate rows

##df = df.drop_duplicates()

















