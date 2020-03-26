from py42.sdk.queries.fileevents.file_event_query import FileEventFilterStringField


class DeviceUsername(FileEventFilterStringField):
    """Class that filters events by Code42 username of device that observed the event."""

    _term = u"deviceUserName"


class OSHostname(FileEventFilterStringField):
    """Class that filters events by Hostname of device that observed the event."""

    _term = u"osHostName"


class PrivateIPAddress(FileEventFilterStringField):
    """Class that filters events by private (lan) IP address of device that observed the event."""

    _term = u"privateIpAddresses"


class PublicIPAddress(FileEventFilterStringField):
    """Class that filters events by public (wan) IP address of device that observed the event."""

    _term = u"publicIpAddress"
