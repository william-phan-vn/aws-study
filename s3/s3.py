import boto3
from botocore import exceptions


class S3Service:
    def __init__(self) -> None:
        self.s3 = boto3.resource('s3')

    def is_file_exist(self, bucket: str, key: str) -> bool:
        try:
            self.s3.Object(bucket, key).load()
            return True
        except exceptions.ClientError as exc:
            return exc.response['Error']['Code'] != '404'
        except Exception:
            return False

    def copy_file(self, from_bucket: str, from_key: str, to_bucket: str, to_key: str) -> None:
        copy_source = {
            'Bucket': from_bucket,
            'Key': from_key
        }
        self.s3.meta.client.copy(copy_source, to_bucket, to_key)
        print('copying file')


s3_service = S3Service()
