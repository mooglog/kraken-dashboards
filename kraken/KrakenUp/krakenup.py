import datetime

class CallRateLimiter:
    from . import tiers

    permit_call_public = True
    permit_call_private = True

    def __init__(self, tier, api_type):
        self.tier = tier
        self.api_type = api_type
        self._public_calls = 0
        self._private_calls = 0
        self.time_of_last_public_query = datetime.datetime.now()
        self.time_of_last_query = datetime.datetime.now()