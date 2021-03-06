# WARNING: you are on the master branch, please refer to the examples on the branch that matches your `cortex version`

import boto3
import pickle

labels = ["setosa", "versicolor", "virginica"]


class PythonPredictor:
    def __init__(self, config):
        s3 = boto3.client("s3")
        s3.download_file(config["bucket"], config["key"], "model.pkl")

        self.model = pickle.load(open("model.pkl", "rb"))

    def predict(self, payload):
        measurements = [
            [
                sample["sepal_length"],
                sample["sepal_width"],
                sample["petal_length"],
                sample["petal_width"],
            ]
            for sample in payload
        ]

        label_ids = self.model.predict(measurements)
        return [labels[label_id] for label_id in label_ids]
