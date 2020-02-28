import json


class Py42Response(object):
    def __init__(self, requests_respsonse, json_key):
        self._response = requests_respsonse
        self._json_key = json_key
        self._dict = None

    def __getitem__(self, key):
        if not self._dict:
            self._dict = json.loads(self._response.text)

        data_root = self._dict.get("data") or self._dict
        return data_root[key]

    def __str__(self):
        return self._response.text

    @property
    def raw(self):
        return self._response
