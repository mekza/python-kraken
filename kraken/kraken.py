# coding=utf-8

""" kraken wrapper

All of API calls are created and responses parsed in this file.

>>> from kraken import Kraken
>>> Kraken.api_key = 'your-key'
>>> Kraken.api_secret = 'your-secret'
"""

import requests
import json

version = "0.0.1"

class KrakenException(Exception):
    """ Base error. """
    def __init__(self, message, result=None):
        super(KrakenException, self).__init__(message)
        self.result = result

class BadRequest(KrakenException):
    pass

class AuthenticationError(KrakenException):
    pass

class BadGatewayError(KrakenException):
    pass

class ResourceNotFound(KrakenException):
    pass

class ServerError(KrakenException):
    pass

class ServiceUnavailableError(KrakenException):
    pass

class RequestTooLarge(KrakenException):
    pass

class FileTypeUnsupported(KrakenException):
    pass

class UnprocessableEntity(KrakenException):
    pass

class TooManyRequests(KrakenException):
    pass

def raise_errors_on_failure(response):
    if response.status_code == 404:
        raise ResourceNotFound("Not found.")
    elif response.status_code == 400:
        raise BadRequest("Incoming request body does not contain a valid JSON object.")
    elif response.status_code == 401:
        raise AuthenticationError("Unnknown API Key. Please check your API key and try again")
    elif response.status_code == 413:
        raise RequestTooLarge("File size too large.")
    elif response.status_code == 415:
        raise FileTypeUnsupported("File type not supported.")
    elif response.status_code == 422:
        raise UnprocessableEntity("You need to specify either callback_url or wait flag.")
    elif response.status_code == 429:
        raise TooManyRequests("Overage usage limit hit.")
    elif response.status_code == 500:
        raise ServerError("Kraken has encountered an unexpected error and cannot fulfill your request")
    elif response.status_code == 502:
        raise BadGatewayError("Bad gateway.")
    elif response.status_code == 503:
        raise ServiceUnavailableError("Service unavailable.")
    
    return response

class Kraken(object):
    """Kraken API wrapper"""
    
    api_key = None
    api_secret = None
    api_version = 1
    api_endpoint = 'https://api.kraken.io/v' + str(api_version) + '/'
    timemout = 15

    @classmethod
    def url(cls, url, wait=True, callback_url=None):
        """
        url classmethod
        returns dict
        """
        
        # Kraken API only returns 200 OK even if it fails.
        if not wait and not callback_url:
            raise KrakenException("You need to specify a callback URL.")

        # Kraken API only returns 200 OK even if it fails.
        if wait and callback_url:
            raise KrakenException("You need to specify either callback_url or wait flag.")

        data = {
            "auth": {
                "api_key":cls.api_key,
                "api_secret":cls.api_secret
            },
            "url":url,
        }
        
        if wait:
            data['wait'] = wait

        if callback_url:
            data['callback_url'] = callback_url

        headers = {
            'User-Agent': 'kraken-python/' + version,
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        
        api_url = cls.api_endpoint + 'url'

        api_call = requests.post(api_url, headers=headers, data=json.dumps(data))
        api_call = raise_errors_on_failure(api_call)
        return api_call.json()


    @classmethod
    def upload(cls):
        pass
            