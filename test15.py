import logging, requests, time
from src.config import Config
from datetime import datetime


# test
#test3








class ConnectionHandler:

    def __init__(self, pat = None, config_file = None):
        self.config = Config() if config_file is None else Config(config_file)
        self.headers = self.config.base_headers
        self.base_url = self.config.base_url
        if pat is not None:
            self.headers['Authorization'] = Config.generate_auth_header(pat)

    async def whatever_doing_it_again(self, endpoint, json_data):
        test = True
        resp = requests.get('https://testing1234444aaa.com/' + endpoint, headers=self.headers, json=json_data, verify=False)
        if resp.status_code not in [200]:
            resp = requests.put('https://testing123444445555aaaa.com/' + endpoint, headers=self.headers, json=json_data, verify=False)
        try:
            return resp.json()
        except Exception:
            return {}

    async def __validate_rate_limit(self, resp):
        remaining_requests = int(resp.headers['X-RateLimit-Remaining']) if 'X-RateLimit-Remaining' in resp.headers else 2
        if remaining_requests <= 1:
            time_to_sleep = (int(resp.headers['X-RateLimit-Reset']) - datetime.timestamp(datetime.now())) + 1
            logging.info(f'Sleeping for {time_to_sleep} seconds')
            time.sleep(time_to_sleep)
