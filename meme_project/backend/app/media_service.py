from minio import Minio
from core.config import settings

client = Minio(
    settings.MINIO_ENDPOINT,
    access_key=settings.MINIO_ACCESS_KEY,
    secret_key=settings.MINIO_SECRET_KEY,
    secure=False
)

def upload_file(file_name, file_data):
    if not client.bucket_exists(settings.MINIO_BUCKET):
        client.make_bucket(settings.MINIO_BUCKET)
    client.put_object(settings.MINIO_BUCKET, file_name, file_data, length=-1, part_size=10*1024*1024)
    return client.get_object_url(settings.MINIO_BUCKET, file_name)

def get_file(file_name):
    return client.get_object(settings.MINIO_BUCKET, file_name)
