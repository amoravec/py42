from py42._internal.compat import str
from py42.clients import BaseClient


class FileEventClient(BaseClient):
    """A client for searching Code42 Forensic File Search events."""

    def search(self, query):
        """Searches for file events matching query criteria.
        `REST Documentation: <https://forensicsearch-east.us.code42.com/forensic-search/queryservice/swagger-ui.html#/file-event-controller/searchEventsUsingPOST>`__

        Args:
            query (str): Forensic File Search query in JSON format.
        """
        query = str(query)
        uri = u"/forensic-search/queryservice/api/v1/fileevent"
        return self._session.post(uri, data=query)
