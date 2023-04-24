from common.spark.session import SparkBuilder
import argparse


def get_spark_session(dataset_name):
    spark_session = SparkBuilder(dataset_name).get_spark_session()
    return spark_session


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-name", required=True)

    args = parser.parse_args()
    dataset_name = args.dataset_name

    spark_session = get_spark_session(dataset_name)
