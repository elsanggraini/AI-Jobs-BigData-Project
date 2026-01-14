from pyspark.sql import SparkSession
from pyspark.sql.functions import when

# 1. Inisialisasi SparkSession
spark = SparkSession.builder.appName("Clean_AI_Jobs").getOrCreate()

# 2. Baca file CSV
df = spark.read.csv("ai_job_dataset.csv", header=True, inferSchema=True)

# 3. Hapus baris duplikat
df = df.dropDuplicates()

# 4. Hapus kolom yang tidak penting 
df = df.drop(
    "salary_currency",
    "application_deadline",
    "posting_date",
    "job_description_length",
    "required_skills"
)

# 5. Buat kolom remote_type
df = df.withColumn("remote_type", when(df.remote_ratio == 0, "Onsite")
                                  .when(df.remote_ratio == 50, "Hybrid")
                                  .when(df.remote_ratio == 100, "Remote")
                                  .otherwise("Unknown"))

# 6. Hapus kolom remote_ratio
df = df.drop("remote_ratio")

# 7. Tampilkan data
# df.show()

# Urutkan gaji terendah (ascending)
df.orderBy(df.salary_usd.asc()).show(15)


# 8. Simpan ke CSV
# df.coalesce(1).write.csv("output/clean_ai_jobs_single", header=True, mode="overwrite")

# Stop Spark session setelah selesai
spark.stop()
