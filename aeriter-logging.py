import hashlib
from libcloud.storage.types import Provider
from libcloud.storage.providers import get_driver
import boto

aws_access_key_id = boto.config.get("Credentials", "aws_access_key_id")
aws_secret_access_key = boto.config.get("Credentials", "aws_secret_access_key")

print aws_access_key_id
print aws_secret_access_key

container_name = "aeriter-logging"
path = ""
delete_files = False

storage_driver = get_driver(Provider.S3)
provider = storage_driver(aws_access_key_id, aws_secret_access_key)
container = provider.get_container(container_name)
container_objects = provider.list_container_objects(container)

print container_objects
