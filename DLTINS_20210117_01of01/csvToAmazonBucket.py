import boto3  # pip install boto3
access_key = 'AKIAXX5B6JMUHJKCPXEC'
bucket_name = 'steelseye'
secret_access_key = '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'

import boto3
import logging
from botocore.exceptions import NoCredentialsError
def fileLogging():
    """Initialize basic configuration for logging."""
    logging.basicConfig(
        filename="aws_upload.txt",
        filemode='w',
        format='[%(asctime)s]: %(message)s',
        level=logging.INFO
    )

''' function to upload csv file on AWS s3 bucket'''
def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=access_key,
                      aws_secret_access_key=secret_access_key)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        logging.info("Upload Successful")
        return True
    except FileNotFoundError:
        logging.error("The file was not found")
        return False
    except NoCredentialsError:
        logging.warning("Credentials not available")
        return False


uploaded = upload_to_aws('DLTINS_20210117_01of01.csv', bucket_name, 'DLTINS_20210117_01of01.csv')
