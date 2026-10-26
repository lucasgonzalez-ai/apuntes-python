task-based sections. Each section has a quick-reference table and a short, copy-ready code ¥ What's inside: the 100 Pandas functions data scientists reach for most, grouped into 10 example. Every example assumes the setup below, where df is a DataFrame. 

Setup used in all examples 

import pandas as pd 

import numpy as np 

df = pd.read_csv("data.csv") 

# @ Import / Export 

|#|Function|What itdoes|
|---|---|---|
|1|pd. read_csv()|Load aCSV file|
|2|pd. read_excel()|Load an Excel file|
|3|pd. read_json()|Load aJSON file|
|4|pd. read_sql()|Load data from a SQL query|
|5|pd. read_parquet()|Load a Parquet file|
|6|df.to_csv()|SavetoCSV|
|7|df.to_excel()|Save to Excel|
|8|df.to_json()|Save toJSON|
|9|df.to_sql()|Write a DataFrame to a database|
|10|df.to_parquet()|SavetoParquet|



Load and save in one go 

df = pd.read_csv("sales.csv") df = pd.read_excel("sales.xlsx", sheet_name="Q1") df = pd.read_json("sales.json") df = pd.read_sql("SELECT * FROM orders", conn) df = pd.read_parquet("sales.parquet") df.to_csv("clean.csv", index=False) df.to_excel("clean.xlsx", index=False) df.to_json("clean.json", orient="records") df.to_sql("orders", conn, if_exists="replace") df .to_parquet("clean.parquet") 

A asWarning:an extra, Passunnamed index=Falsecolumn. to to_csv() and to_excel() unless you want the index saved 

# @ Inspecting Data 

|#|Function|What itdoes|
|---|---|---|
|11|head()|First rows (5 by default)|
|12|tail()|Last rows|
|13|info()|Column dtypes and non-null counts|
|14|describe()|Summary statistics|
|15|shape|(rows, columns)|
|16|columns|Column names|
|17|dtypes|Data type of each column|
|18|sample()|Random rows|
|19|nunique()|Count of unique values|
|20|value_counts()|Frequency ofeach value|
|21|unique()|Array of unique values|
|22|memory_usage()|Memoryusedpercolumn|



## Quick first look at a dataset 

df .head() # first 5 rows df.tail(3) # last 3 rows df.info() # dtypes + non-null counts df .describe() # count, mean, std, min, max df.shape # (rows, columns) df.columns # column names df .dtypes # type of each column df.sample(5) # 5 random rows df[“city"].nunique() # number of unique cities df["city"].value_counts() # frequency of each city df["city"].unique() # array of unique cities df.memory_usage(deep=True) # bytes per column 

© Key insight: Run info() first on any new dataset. One call shows dtypes and null counts, so you know what needs cleaning before you do anything else. 

# ® Missing Values 

|#|Function|What itdoes|
|---|---|---|
|23|isnull()|Flag missing values|
|24|notnull()|Flag non-missing values|
|25|isna()|Alias of isnull()|
|26|dropna()|Remove rows or columnswith nulls|
|27|fillna()|Fill nulls with a value|
|28|ffill()|Forward fill from the previous value|
|29|bfill()|Backward fill from the next value|
|30|interpolate()|Estimate missing values|
|31|replace()|Replacespecificvalues|



## Find, drop and fill missing values 

df.isnull().sum() # nulls per column df.notnull().sum() # non-nulls per column df.isna().mean() # share of nulls per column df.dropna(subset=["age"]) # drop rows missing age df["age"].fillna(0) # fill nulls with 0 df. ffill() # carry last value forward df. bfill() # pull next value backward df["“temp"].interpolate() # estimate the gaps df.replace("N/A", np.nan) # standardize null markers 

A wipeWarning:out most dropna() of yourwith data. noCheck argumentsdf.isna().sum() deletes every rowfirst, thator use has evensubset=. one null, which can 

# ® Selection / Filtering 

|#|Function|What itdoes|
|---|---|---|
|32|loc[]|Label-based selection|
|33|iloc{]|Position-based selection|
|34|at[]|Fast single-value access|
|35|query()|Filter using a string expression|
|36|filter()|Select columns by name pattern|
|37|isin()|Match against a list ofvalues|
|38|between()|Values within a range|
|39|nlargest()|Top N values|
|40|nsmallest()|BottomN values|
|41|select_dtypes()|Pickcolumnsbydtype|



### Select and filter rows and columns 

df.loc{0, "“name"] # by label df.iloc[0:5, 0:3] # by position df.at[0, "name"] # fastest single value df.query("age > 30 and city == 'Delhi'") df.filter(like="date") # columns containing "date" df(df["city"].isin(["Delhi", "Noida"])] df[df["age"].between(20, 30)] df.nlargest(5, "“salary") # top 5 by salary df.nsmallest(5, “salary") # bottom 5 by salary df .select_dtypes(include="number" ) 

(OF df.loc(df["age"]Key insight: Use loc> for30, labels“name"], and ilocfilters forrows positions.and picks A booleancolumns maskin one insidst **e** loc,p. like 

# ® Cleaning / Transforming 

|#|Function|What itdoes|
|---|---|---|
|42|drop()|Remove rows or columns|
|43|rename()|Rename labels|
|44|astype()|Change dtype|
|45|drop_duplicates()|Remove duplicate rows|
|46|duplicated()|Flag duplicate rows|
|47|assign()|Add new columns|
|48|apply()|Apply a function along an axis|
|49|map()|Element-wise mapping on a Series|
|50|transform()|Same-shaped output (great with groupby)|
|51|clip()|Cap values at limits|
|52|round()|Roundnumbers|



### Clean and transform columns 

df .drop(columns=["temp"]) df.rename(columns={"dob": "birth_date"}) df["“age"] = df["age"].astype(int) df.drop_duplicates(subset=["id"]) df .duplicated().sum() df.assign(total=df["qty"] * df["price"]) df.apply(lambda r: r["a"] + r["b"], axis=1) df["grade"].map({"A": 1, "B": 2}) df.groupby("city")["sales"].transform("mean") df["score"].clip(0, 100) df["“price"].round(2) 

A Warning: apply() with axis=1 loops row by row and gets slow on big data. Prefer vectorized operations such as df["a"] + df["b"] whenever you can. 

# ® Sorting / Indexing 

|#|Function|What itdoes|
|---|---|---|
|53|sort_values()|Sort by values|
|54|sort_index()|Sort by index|
|55|set_index()|Makea columnthe index|
|56|reset_index()|Restore the default index|
|57|reindex()|Conformtoanewindex|



#### Sort and re-index 

df.sort_values("salary", ascending=False) df.sort_index() df = df.set_index("id") df = df.reset_index(drop=True) df = df.reindex(range(10), fill_value=0) 

# ® Aggregation / Statistics 

|#<br>|Function<br>|What itdoes<br>|
|---|---|---|
|| 58|7groupby0.|Split-apply-combine|
|59|agg()|Multiple aggregations at once|
|60|sum()|Total|
|61|mean()|Average|
|62|median()|Middle value|
|63|mode()|Most frequent value|
|64|std()|Standard deviation|
|65|var()|Variance|
|66|min()|Minimum|
|67|max()|Maximum|
|68|count<br>()|Non-null count|
|69|cumsum()|Cumulative sum|
|70|cumprod()|Cumulative product|
|71|pct_change()|Percentage change|
|72|diff()|Difference from the previous row|
|73|rank()|Rank values|
|74|corr()|Correlation matrix|
|75|cov()|Covariance|
|76|quantile()|Percentiles|
|77|idxmax()|Index of the max value|
|78|idxmin()|Indexoftheminvalue|



## Group and summarize 

df.groupby("city")["sales"].sum() df.groupby("city").agg({"sales": ["sum", "mean"]}) df["sales"].sum() df["sales"].mean() df["sales"] .median() df["sales"].mode() df["sales"].std() df["sales"].var() df["sales"].min() df["sales"] .max() df["sales"].count() 

## Trends, ranks and relationships 

df["sales"].cumsum() df["growth"].cumprod() df["sales"].pct_change() df["sales"].diff() df["sales"].rank(ascending=False) df.corr(numeric_only=True) df .cov(numeric_only=True) df["sales"].quantile(0.9) df["sales"].idxmax() df["sales"].idxmin() 

compute stats for each group, and combine the results in a single line. | (Cj Key insight: groupby() + agg() is the most-used pattern in analysis: split bya category, 

# ® Combining / Reshaping 

|#|Function|Whatitdoes|
|---|---|---|
|79|pd.merge()|SQL-style joins|
|80|pd.concat()|Stack DataFrames|
|81|join()|Join on the index|
|82|pivot()|Reshape long towide|
|83|pivot_table()|Pivotwith aggregation|
|84|melt()|Reshape wide to long|
|85|stack()|Columns to rows|
|86|unstack()|Rows to columns|
|87|pd.crosstab()|Frequency cross-tab|
|88|explode()|Listitemstoseparaterows|



## Join, reshape and cross-tabulate 

pd.merge(orders, customers, on="cust_id", how="left") pd.concat([jan, feb], ignore_index=True) orders. join(customers) df .pivot(index="date", columns="city", values="sales") df.pivot_table(index="city", values="sales", aggfunc="sum") df.melt(id_vars="city", var_name="month", value_name="amt") df.stack() df .unstack() pd.crosstab(df["city"], df["gender"]) df .explode("tags") 

A Warning:len(df) before A wrongandkeyafter, or how=or pass typevalidate="one_to_one". can silently duplicate or drop rows in a merge. Compare 

# @ String Operations 

|#|Function<br>What itdoes|
|---|---|
|89|str.lower()<br>/ str.upper()<br>Change case|
|90|str.strip()<br>Trim whitespace|
|91|str.contains()<br>Pattern search|
|92|str.replace()<br>Replace text|
|93|str.split()<br>Split into parts|
|lean <br>df[|text columns<br>"name"].str.lower()|
|df[|"name"].str.upper()|
|df[|"name"].str.strip()|
|df[|"email"].str.contains("@gmail")|
|df[|"phone"].str.replace("-",<br>"")|
|df[|"name"].str.split("<br>")|



### Clean text columns 

# ® Datetime / Window / Binning 

|#|Function|What itdoes|
|---|---|---|
|94|pd.to_datetime()|Convert to datetime|
|95|dt accessor|Extract date parts: dt.year, dt.month, dt.dayofweek|
|96|resample()|Time-based grouping|
|97|rolling()|Moving-window calculations|
|98|shift()|Lag or lead values|
|99|pd.cut()<br>/ pd.qcut()|Bin values into ranges or quantiles|
|100|pd.get_dummies()|One-hotencoding|



|Section|#|Count|Go-tofunctions|Use itto|
|---|---|---|---|---|
|Import/Export|1-10|10|fengces read_sql,|Getdata inand out|
|5<br>Inspecting Data|11-22|12|head,<br>info,<br>describe,<br>value_counts|Understandanewdataset|
|Missing Values|23-31|9|isnull, dropna, fillna|Find and handle nulls|
|Selection / Filtering|32-41|10|Loc, floc, query, isin|Picktherowsandcolumns<br>you need|
|Cleaning /<br>Transforming|42-52|uu|drop, rename, astype,<br>apply|Fix types, namesand<br>duplicates|
|Sorting /Indexing|53-57|5|sort_values, set_index|omerfows.andmefiage<br>the index|
|Aggregation /<br>My<br>Statistics|58-78|21|groupby, agg, corr,<br>rank|:<br>Summarize and compare<br>e|
|Combining /<br>Reshaping|79-88|10|Bence, .concat,<br>pivot_table, melt|Joinand reshape<br>tables<br>a<br>jesnape|
|;<br>-<br>String Operations|89-93|5|str.contains,<br>str.replace|Clean textcolumns|
|Datetime /Window/<br>Binning|94-100|7|to_datetime, resample,<br>rolling|‘<br>-<br>5<br>:<br>Time series, bins,encoding|
|Total|1-100|100|||



