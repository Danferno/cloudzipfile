''' Provides the abstracted methods for each supported cloud client '''
from azure.storage.blob import BlobClient
import io

class AzureClient:
    @staticmethod
    def getSize(blobClient:BlobClient):
        return blobClient.get_blob_properties()['size']

    @staticmethod
    def partialDownloadToBuffer(blobClient:BlobClient, offset, length, max_concurrency=8):
        return io.BytesIO(blobClient.download_blob(offset=offset, length=length, max_concurrency=max_concurrency).content_as_bytes())