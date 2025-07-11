from pyspark.sql import SparkSession

# Create or get the SparkSession; this creates a SparkContext internally if not already present.
spark = SparkSession.builder \
    .appName("WordCountBasic") \
    .master("local[*]") \
    .config("spark.hadoop.fs.native.lib.disable", "true") \
    .getOrCreate()

# Get the SparkContext from the SparkSession; do not create a new one.
sc = spark.sparkContext

# Define your RDD operations
file_rdd1 = sc.textFile(r"C:\Users\siddh\Desktop\MS_Study\Spring 2025\Data Intensive Computing\Assignment 2\book1.txt")
file_rdd2 = sc.textFile(r"C:\Users\siddh\Desktop\MS_Study\Spring 2025\Data Intensive Computing\Assignment 2\book2.txt")
combined_rdd = file_rdd1.union(file_rdd2)
words_rdd = combined_rdd.flatMap(lambda line: line.split())
word_counts = words_rdd.map(lambda w: (w, 1)).reduceByKey(lambda a, b: a + b)

# Print sample output
print("Sample Word Counts (first 10):")
for word, cnt in word_counts.take(10):
    print(f"{word} -> {cnt}")

# Save the output
word_counts.saveAsTextFile("output1.txt")

# Stop the SparkSession (and its SparkContext)
spark.stop()
