"""
GovTrack API library for Python.

Based on https://github.com/markgx/govtrack-node/
"""

import json
import requests
import urllib

GOV_TRACK_API_BASE_PATH = 'http://www.govtrack.us/api/v2/'


class GovTrackClient(object):

    """
    Turns a dictionary of filters into a url query parameter string in the form of ?key1=value1&key2=value2&key3=value3.
    If the dictionary contains the key 'id', begin the query parameter string with the 'id' as a string. If the 'id' is
    an integer, return the integer as a string. If the params parameter is not an integer or a dictionary, the function
    will raise an AttributeError when it tries to access .items() on params.

    Args:
        params (dict or int): Either a dict of filters, or an integer representing an ID number
    """
    def _url_encode_params(self, params):
        _id = None
        params_copy = None

        if type(params) is int:
            _id = params
        else:
            params_copy = dict()
            for key, value in params.items():
                if key != 'id':
                    params_copy[key] = value
                else:
                    _id = value

        ret = ''

        if _id:
            ret += str(_id)

        if params_copy:
            ret += '?' + urllib.urlencode(params_copy)

        return ret

    """
    Makes the call to the GovTrack.us API. If something goes wrong it will let all relevant exceptions occur.

    Args:
        sub_path (str): last section of the GovTrack API route that defines which endpoint we would like to hit
    """
    def _make_call(self, sub_path):
        url = GOV_TRACK_API_BASE_PATH + sub_path
        response = requests.get(url).content
        return json.loads(response)

    def bill(self, params):
        return self._make_call('bill/' + self._url_encode_params(params))

    def cosponsorship(self, params):
        return self._make_call('cosponsorship/' + self._url_encode_params(params))

    def person(self, params):
        return self._make_call('person/' + self._url_encode_params(params))

    def role(self, params):
        return self._make_call('role/' + self._url_encode_params(params))

    def vote(self, params):
        return self._make_call('vote/' + self._url_encode_params(params))

    def vote_voter(self, params):
        return self._make_call('vote_voter/' + self._url_encode_params(params))
