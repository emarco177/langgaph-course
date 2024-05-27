# Import the Quix Streams modules for interacting with Kafka:
from quixstreams import Application
from quixstreams.models.serializers.quix import JSONSerializer, SerializationContext

# (see https://quix.io/docs/quix-streams/v2-0-latest/api-reference/quixstreams.html for more details)

# Import additional modules as needed
import pandas as pd
import random
import time
import os

# for local dev, load env vars from a .env file
from dotenv import load_dotenv

load_dotenv()

# Create an Application
app = Application(
    quix_sdk_token=os.getenv("QUIX_SDK_TOKEN"),
    consumer_group="csv_sample",
    auto_create_topics=False,
)
# Define a serializer for messages, using JSON Serializer for ease
serializer = JSONSerializer()

# Define the topic using the "output" environment variable
topic_name = os.environ["output"]
topic = app.topic(topic_name)

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))
# Construct the path to the CSV file
csv_file_path = os.path.join(script_dir, "demo-data.csv")


# this function loads the file and sends each row to the publisher
def read_csv_file(file_path: str):
    """
    A function to read data from a CSV file in an endless manner.
    It returns a generator with stream_id and rows
    """

    # Read the CSV file into a pandas.DataFrame
    print("CSV file loading.")
    df = pd.read_csv(file_path)
    print("File loaded.")

    # Get the number of rows in the dataFrame for printing out later
    row_count = len(df)

    # Generate a unique ID for this data stream.
    # It will be used as a message key in Kafka
    stream_id = f"CSV_DATA_{str(random.randint(1, 100)).zfill(3)}"

    # Get the column headers as a list
    headers = df.columns.tolist()

    # Continuously loop over the data
    while True:
        # Print a message to the console for each iteration
        print(f"Publishing {row_count} rows.")

        # Iterate over the rows and convert them to
        for _, row in df.iterrows():
            # Create a dictionary that includes both column headers and row values
            row_data = {header: row[header] for header in headers}

            # add a new timestamp column with the current data and time
            row_data["Timestamp"] = time.time_ns()

            # Yield the stream ID and the row data
            yield stream_id, row_data

        print("All rows published")

        # Wait a moment before outputting more data.
        time.sleep(1)


def main():
    """
    Read data from the CSV file and publish it to Kafka
    """

    # Create a pre-configured Producer object.
    # Producer is already setup to use Quix brokers.
    # It will also ensure that the topics exist before producing to them if
    # Application.Quix is initiliazed with "auto_create_topics=True".
    producer = app.get_producer()

    with producer:
        # Iterate over the data from CSV file
        for message_key, row_data in read_csv_file(file_path=csv_file_path):
            # Serialize row value to bytes
            serialized_value = serializer(
                value=row_data, ctx=SerializationContext(topic=topic.name)
            )

            # publish the data to the topic
            producer.produce(
                topic=topic.name,
                key=message_key,
                value=serialized_value,
            )


if __name__ == "__main__":
    try:
        main()
        print("Done!")
    except KeyboardInterrupt:
        print("Exiting.")