import pyspark
from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("movie-ratings").getOrCreate()
# load the required csv from the workspace
# required csvs

    # Load movies.csv and ratings.csv (loaded)
    
    # Top 10 highest-rated movies
    # Most-rated movies
    # Average rating per genre
    # Most active users

df_movies = spark.read.format("csv").option("header", True).load("/Volumes/workspace/user_uploads/manual-datasets-upload/movies.csv")
df_ratings = spark.read.format("csv").option("header", True).load("/Volumes/workspace/user_uploads/manual-datasets-upload/ratings.csv")

df_movies.show()
# top 10 highest rated movies
# from the ratings order by the ratings and get the top 10
