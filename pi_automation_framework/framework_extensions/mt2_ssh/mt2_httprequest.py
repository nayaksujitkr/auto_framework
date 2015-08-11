import re
from requests import Session
import requests
import subprocess
import cookielib as cookiejar
import time

class MT2_HttpRequest(Session):

    def __init__(self,  protocol="http", keep_cookie=True):#pixel_server,
        '''
        Constructor
        '''
#         if not re.match("https?", protocol=None):
#             raise ValueError("protocol should be http/https")
#         self.protocol = protocol
        #self.pixel_server = self.protocol + "://" +pixel_server
        self.req = requests.session()
        

    def get(self, url=None, req_type=None, headers=None, params=None, follow_redir=True, cookies=None, basic_check=True):
        if params and not isinstance(params, dict):
            raise Exception("Parameters should be dictionary, got " + str(type(params)))

        if headers and not isinstance(headers, dict):
            raise Exception("Headers should be dictionary, got " + str(type(headers)))

        req = self.req
#         if not url:
#             url = self.pixel_server
#         if req_type:
#             url += req_type

        if cookies:
            result = req.get(url=url, params=params, headers=headers, allow_redirects=follow_redir, cookies=cookies)
        else:
            result = req.get(url=url, params=params, headers=headers, allow_redirects=follow_redir)
        time.sleep(5)
        # Do mt2 basice checks on result
#         if basic_check:
#             pr = ParseResult(result)
#             errors = pr.basic_checks(expected_code=200)
#             assert len(errors) == 0

        return result

    def clear_cookies(self):
        self.req.cookies.clear()
        
    def get_cookies(self):
        return self.req.cookies

    def get_cookie(self, name):
        if not isinstance(name, str):
            raise TypeError("Cookie name should be string, got " + str(type(name)))
        #value = self.req.cookies.get(name)
        value = requests.utils.dict_from_cookiejar(self.req.cookies)[name]
        if not value:
            return None
        else:
            return value

    def check_cookie(self, name, pattern):
        if not isinstance(name, str):
            raise TypeError("Cookie name should be string, got " + str(type(name)))
        cookie = requests.utils.dict_from_cookiejar(self.req.cookies)[name]
        if not cookie:
            raise KeyError
        return re.search(pattern, cookie)