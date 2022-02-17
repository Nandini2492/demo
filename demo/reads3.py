import requests
import os
import json
import pandas as pd
import boto3
from botocore.errorfactory import ClientError
import io
def readS3(AWSAccessKeyId, AWSSecretKey, bucketname, filename, file_type):

    client = boto3.client(
        's3',
        aws_access_key_id=AWSAccessKeyId,
        aws_secret_access_key=AWSSecretKey
    )
    try:
        obj = client.get_object(Bucket= bucketname, Key=filename )
        if file_type == "csv":
            initial_df = pd.read_csv(obj['Body'])  # 'Body' is a key word
        else:
            data = obj['Body'].read()
            initial_df = pd.read_excel(io.BytesIO(data))

        return initial_df
    except ClientError:
        # Not found
        return("not found")
    except Exception as e:
        return str(e)
