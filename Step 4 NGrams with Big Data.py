df = spark.read.csv("hdfs:///user/hadoop/eng_1M_1gram", header=True)


df.describe().show()
df.printSchema()


df.createOrReplaceTempView("ngrams")


data_df = spark.sql("SELECT * FROM ngrams WHERE token = 'data'")
data_df.show()


data_df.write.csv("hdfs:///user/hadoop/eng_1M_1gram_filtered", header=True)

