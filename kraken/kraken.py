# coding=utf-8
import requests
import json
from .helpers import raise_errors_on_failure, KrakenException

class Kraken(object):
    """Kraken API wrapper"""
    __version__ = "0.0.4"
    USER_AGENT = 'python-kraken v{0}'.format(__version__)
    api_version = 'v1'
    timemout = 15
    api_url = 'https://api.kraken.io/{api_version}'.format(api_version=api_version)

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
    
    def make_request(self, endpoint, method, payload=None, params=None, allow_redirects=True):
        if params is None:
            params = {}
        if payload:
            payload['auth'] = {
                "api_key":self.api_key,
                "api_secret":self.api_secret
            }
            payload = json.dumps(payload)

        headers = {
            'User-Agent': self.USER_AGENT,
            'Accept':'application/json',
            'Content-Type':'application/json'
        }
        if method == 'GET':
            r = requests.get(self.api_url + endpoint,
                                params=params,
                                headers=headers,
                                allow_redirects=allow_redirects)
            r = raise_errors_on_failure(r)
        elif method == 'DELETE':
            r = requests.delete(self.api_url + endpoint,
                                   params=params,
                                   data=payload,
                                   headers=headers,
                                   allow_redirects=allow_redirects)
            r = raise_errors_on_failure(r)
        elif method == 'POST':
            r = requests.post(self.api_url + endpoint,
                                 params=params,
                                 data=payload,
                                 headers=headers,
                                 allow_redirects=allow_redirects)
            r = raise_errors_on_failure(r)
        elif method == 'PUT':
            r = requests.put(self.api_url + endpoint,
                                params=params,
                                data=payload,
                                headers=headers,
                                allow_redirects=allow_redirects)
            r = raise_errors_on_failure(r)

        return r.json()

    def url(self, image_url, wait=True, callback_url=None, quality=None, webp=False, lossy=False, 
        resize=None, convert=None, s3_store=None, cf_store=None, azure_store=None):
        
        # Kraken API only returns 200 OK even if it fails.
        if not wait and not callback_url:
            raise KrakenException("You need to specify a callback URL.")

        # Kraken API only returns 200 OK even if it fails.
        if wait and callback_url:
            raise KrakenException("You need to specify either callback_url or wait flag.")

        data = {
            "url":image_url,
        }
        
        if wait:
            data['wait'] = wait

        if callback_url:
            data['callback_url'] = callback_url

        if webp:
            data['webp'] = webp

        if lossy:
            data['lossy'] = lossy

        if quality and quality <= 0:
           KrakenException("Quality should be a number within the range of 1-100.")
        else:
            data['quality'] = quality

        if resize:
            data['resize'] = resize

        if convert:
            data['convert'] = convert

        if s3_store:
            data['s3_store'] = s3_store

        if cf_store:
            data['cf_store'] = cf_store

        if azure_store:
            data['azure_store'] = azure_store

        return self.make_request('url', 'POST', payload=data) 


    def upload(self):
        pass
            