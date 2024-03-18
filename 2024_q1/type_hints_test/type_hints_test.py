"""
@FileName：type_hints_test.py
@Description：
@Author：shenxinyuan
@Time：2024/2/22
"""
from abc import ABCMeta, abstractmethod
from urllib.parse import ParseResult
import typing as t

URI = ParseResult


class StorageClient(metaclass=ABCMeta):
    @abstractmethod
    def sync(self, src: URI, dest: URI) -> None:
        """
        Sync files from a source URI to a destination URI.

        Args:
            src: The source URI.
                For example, s3://bucket/path/to/file or file://path/to/file.
            dest: The destination URI.
                For example, s3://bucket/path/to/file or file://path/to/file.

        Returns:
            None

        Raises:
            ValueError: If the source or destination URI is invalid.
            IOError: If the source or destination URI is not accessible.
        """
        return NotImplemented


class S3StorageClient(StorageClient):
    def __init__(self):
        ...

    def sync(self, src: URI, dest: URI) -> None:
        ...


class AzureCloudStorageClient(StorageClient):
    def __init__(self):
        ...

    def sync(self, src: URI, dest: URI) -> None:
        ...


def create_storage(
        storage_type: t.Literal["s3", "azure"],
    ) -> StorageClient:
    # python 3.10+ 才支持
    # match storage_type:
    #     case "s3":
    #         return S3StorageClient()
    #     case "azure":
    #         return AzureCloudStorageClient()
    if storage_type == "s3":
        return S3StorageClient()
    elif storage_type == "azure":
        return AzureCloudStorageClient()
    else:
        raise ValueError(f"Invalid storage_type: {storage_type}, must be either 's3' or 'azure'")