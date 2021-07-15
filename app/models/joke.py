from typing import Dict
import logging

import requests

logger = logging.getLogger('jokes-logger')


class Joke:
    _url = 'https://official-joke-api.appspot.com/random_joke'

    _fail_resp = {'status': 'failure'}

    @classmethod
    def get_new_joke(cls) -> Dict:

        try:
            req = requests.get(cls._url)
        except requests.exceptions.RequestException as e:
            logger.error(f'request: {cls._url}')
            logger.error(e)
            joke_fail = cls._fail_resp
            return joke_fail

        if req.status_code == 200:
            req_obj = req.json()
            joke = {
                'id': req_obj['id'],
                'type': req_obj['type'],
                'setup': req_obj['setup'],
                'punchline': req_obj['punchline'],
                'status': 'success'
            }
        else:
            joke = cls._fail_resp
        return joke
