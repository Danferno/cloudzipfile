# pytest
# DEBUG: tmpdir = 'data'
from cloudzipfile.cloudzipfile import CloudZipFile
from azure.storage.blob import BlobClient
import os

def test_extractall(tmpdir):
    # Define blob client
    BLOB_URL = 'https://cloudzipfileexamples.blob.core.windows.net/test/files.zip'
    blobClient = BlobClient.from_blob_url(BLOB_URL)

    # Extract specific files
    PATH_OUTPUT = tmpdir
    FILES_DESIRED = ['file1.txt', 'file4.txt']
    cloudZipFile = CloudZipFile(blobClient)
    cloudZipFile.extractall(path=PATH_OUTPUT, members=FILES_DESIRED)

    assert all((file in os.listdir(PATH_OUTPUT) for file in FILES_DESIRED))

if __name__ == '__main__':
    test_extractall('data')