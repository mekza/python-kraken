
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
    elif response.json().get("success") and not response.json().get("success"):
        raise KrakenException(response.json()['message'])

    return response