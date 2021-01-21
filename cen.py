#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import json
import requests
import time

API_URL = "https://censys.io/api/v1"
UID = "37dab833-9e2d-4e25-b26f-7dc5f12943ae"
SECRET = "acOkjvg1AR8PZPIWQi0AFwIn7m9XJRsp"
for page in range(1,10):
  print '\n[++] Grabbing page %s\n'%page
  data = {
  "query":"Repository autonomous_system.country_code: ID",
  "page":page,
  "fields":["ip", "location.country", "autonomous_system.asn"],
  "flatten":True
}
  res = requests.post(API_URL + "/search/ipv4",data=json.dumps(data), auth=(UID, SECRET)).json()
  for i in res['results']:
    print i['ip']
    sv = open('ip-sister.txt','a')
    sv.write('%s\n'%i['ip'])