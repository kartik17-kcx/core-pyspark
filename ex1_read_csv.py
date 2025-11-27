from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Pyspark Core Examples").getOrCreate()

# df = spark.read.option("header", "true").option("inferSchema", "true").csv("dbfs:/Workspace/Users/kartik.choudhary@attryb.com/core-pyspark/resources/zipcodes.csv")

df = spark.read.option("header", "true").csv("file:/Workspace/Users/kartik.choudhary@attryb.com/core-pyspark/resources/zipcodes.csv")

df.printSchema()