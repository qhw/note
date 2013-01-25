#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2012-12-25

@author: qihaiwei
'''
from develop_sdk.weibo import APIClient

APP_KEY = "104116532" #app key
APP_SECRET = "8e4c06def1a74a18ef355cd7a73f43dc" #app secret
CALLBACK_URL = "http://127.0.0.1/home/" #callback_url

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url() #TODO: redirect to url
code = "cb42a89f2417d2415c90dde5a001860e"
r = client.request_access_token(code)
access_token = r.access_token
expires_in = r.expires_in
client.set_access_token(access_token, expires_in)
if __name__ == '__main__':
  print url
  print client.statuses.user_timeline.get()
  print client.statuses.update.post(status=u'李欣欣')