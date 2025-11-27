# quick start
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

# dataframe creation
# creating a pyspark dataframe from a list of rows
from datetime import datetime, date
import pandas as pd
from pyspark.sql import Row

# without schema
df = spark.createDataFrame([
    Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
    Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
    Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
])
# df

# with schema
df = spark.createDataFrame([
    (1, 2., 'string1', date(2000, 1, 1), datetime(2000, 1, 1, 12, 0)),
    (2, 3., 'string2', date(2000, 2, 1), datetime(2000, 1, 2, 12, 0)),
    (3, 4., 'string3', date(2000, 3, 1), datetime(2000, 1, 3, 12, 0))
], schema='a long, b double, c string, d date, e timestamp')
# df

# from pandas dataframe 
pandas_df = pd.DataFrame({
    'a': [1, 2, 3],
    'b': [2., 3., 4.],
    'c': ['string1', 'string2', 'string3'],
    'd': [date(2000, 1, 1), date(2000, 2, 1), date(2000, 3, 1)],
    'e': [datetime(2000, 1, 1, 12, 0), datetime(2000, 1, 2, 12, 0), datetime(2000, 1, 3, 12, 0)]
})

# df = spark.createDataFrame(pandas_df)
# df.show()
# df.printSchema()



# df.collect()

# the driver cannot handle huge data coming from the executors altogether(out of memory issue) , hence to view this use tail or take
# Summary Table (Fastest to Slowest)
# Method	What it returns	Action?	Good for	Danger
# show()	prints table	Yes	Debug quick preview	Can't use output in code
# take(n)	first n rows	Yes	Safe small samples	none
# tail(n)	last n rows	Yes	End samples	slow for large tables
# collect()	ALL rows	Yes	Tiny datasets only	crashes driver
# df.show(1, vertical=True)


from pyspark.sql import Column
from pyspark.sql.functions import upper


# take a column and return another dataframe
# df.select(df.a).show()

# assign a new column instance
# df.withColumn('upper_c', upper(df.c)).show()

# to select a subset of rows
# df.filter(df.a == 1).show()


# applying a function
from pyspark.sql.functions import pandas_udf


@pandas_udf('long')
def pandas_plus_one(series: pd.Series) -> pd.Series:
    return series + 1


# df.select(pandas_plus_one(df.a)).show()

# another way -> df.mapInPandas which allows users to directly use the APIs in a pandas df without any restrictions
def pandas_filter_function(itr):
    for pandas_df in itr:
        yield pandas_df[pandas_df.a == 1]

# df.mapInPandas(pandas_filter_function, schema=df.schema).show()


# grouping data

df = spark.createDataFrame([
    ['red', 'banana', 1, 10], ['blue', 'banana', 2, 20], ['red', 'carrot', 3, 30],
    ['blue', 'grape', 4, 40], ['red', 'carrot', 5, 50], ['black', 'carrot', 6, 60],
    ['red', 'banana', 7, 70], ['red', 'grape', 8, 80]], schema=['color', 'fruit', 'v1', 'v2'])
# df.show()


# grouping and applying the average function to the resulting groups
# df.groupBy('color').avg().show()


def plus_mean(pandas_df):
    return pandas_df.assign(v1=pandas_df.v1 - pandas_df.v1.mean())

df.groupby('color').applyInPandas(plus_mean, schema=df.schema).show()