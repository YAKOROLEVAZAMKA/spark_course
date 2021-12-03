from pyspark.sql import SparkSession
from src.conf import TARGET_TABLE, SAVED_TABLE_SQL

import pyspark.sql.functions as f


# spark settings
spark = SparkSession.builder\
    .config("spark.driver.memory", "2G") \
    .config("spark.jars", "jars/postgresql-42.3.1.jar") \
    .getOrCreate()

# connection url
url = "jdbc:postgresql://postgresql:5432/postgres"

# query
sql_query = """
(
    SELECT age,
           count(*) rows_amount
FROM {}
GROUP BY 1
) t
""".format(TARGET_TABLE)

# load query
df = spark.read\
    .option("driver", "org.postgresql.Driver")\
    .format("jdbc")\
    .option("url", url)\
    .option("user", "p_user")\
    .option("password", "password123")\
    .option("dbtable", sql_query)\
    .option("fetchsize", 10000)\
    .load()

# save to csv
df.repartition(1).write.mode("overwrite").format("com.databricks.spark.csv").save(SAVED_TABLE_SQL)
