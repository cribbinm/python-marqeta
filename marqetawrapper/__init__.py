import os
import requests

MARQETA_USERNAME = os.environ.get('MARQETA_USERNAME', None)
MARQETA_PASSWORD = os.environ.get('MARQETA_PASSWORD', None)

class APIKeyMissingError(Exception):
    pass

if MARQETA_USERNAME is None or MARQETA_PASSWORD is None:
    raise APIKeyMissingError(
        "All methods require an API key. See "
        "https://www.marqeta.com/api-explorer "
        "for how to retrieve an authentication token from "
        "Marqeta"
    )
session = requests.Session()
session.auth = (MARQETA_USERNAME, MARQETA_PASSWORD)
# session.auth['api_key'] = TMDB_API_KEY

from .api import Users