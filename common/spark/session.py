from pyspark.sql import SparkSession

class SparkBuilder:
    def __init__(self, app_name):
        self.app_name = app_name

    def get_spark_session(self):
        spark_session = SparkSession.builder.appName(self.app_name).enableHiveSupport().getOrCreate()
        return spark_session
