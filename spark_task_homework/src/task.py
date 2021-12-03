from pyspark.sql import SparkSession
from src.conf import TARGET_TABLE, SAVED_TABLE

import pyspark.sql.functions as f

# spark settings
spark = SparkSession.builder\
    .config("spark.driver.memory", "2G") \
    .config("spark.jars", "jars/postgresql-42.3.1.jar") \
    .getOrCreate()

# connection url
url = "jdbc:postgresql://postgresql:5432/postgres"

# load query
df = spark.read\
    .option("driver", "org.postgresql.Driver")\
    .format("jdbc")\
    .option("url", url)\
    .option("user", "p_user")\
    .option("password", "password123")\
    .option("dbtable", TARGET_TABLE)\
    .option("fetchsize", 10000)\
    .explain()\
    .load()

# group df
df_grouped = df\
.groupBy("age")\
.agg(
    f.count("*").alias("rows_amount")
    )\
.explain()

# save to csv
df_grouped.repartition(1).write.mode("overwrite").format("com.databricks.spark.csv").save(SAVED_TABLE)
#df_grouped.write.csv(SAVED_TABLE)



