from py42.base_classes import BaseClient
from py42.clients.storage.archive import StorageArchiveClient
from py42.clients import StorageSecurityClient


class StorageClient(BaseClient):
    def __init__(self, session):
        super(StorageClient, self).__init__(session)
        self._archive_client = StorageArchiveClient(session)
        self._security_client = StorageSecurityClient(session)

    @property
    def archive(self):
        return self._archive_client

    @property
    def security(self):
        return self._security_client
