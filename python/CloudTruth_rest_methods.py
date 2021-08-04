#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright (c) 2021 CloudTruth, Inc
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#

import argparse
import getpass
import json
import requests

# Disable SSL warnings
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def parse_args():
    '''Parse command line arguments'''

    parser = argparse.ArgumentParser()

    parser.add_argument('-t', '--token',
                        required=False,
                        help="Specify the API Acces Token")

    parser.add_argument('-e', '--environments',
                        action='store_true',
                        required=False,
                        help="Get environments")

    args = parser.parse_args()

    if not args.token:
        args.token = getpass.getpass(("Please enter your API Access Token: "))
    return args


def invoke_method(token, uri, method, task):
    '''Invoke RESTful method'''

    headers = {'Authorization': f'Api-Key {token}'}

    resource = f'https://api.cloudtruth.io/api/v1/{uri}'

    if method == "GET":
        request = requests.get(url=resource,
                               headers=headers)
    if method == "POST":
        request = requests.post(url=resource,
                                headers=headers,
                                data=json.dumps(task))
    if method == "PUT":
        request = requests.put(url=resource,
                               headers=headers,
                               data=json.dumps(task))
    print(json.dumps(request.json(), indent=4, sort_keys=True))
    return request.json()


def main():
    '''Main'''
    args = parse_args()
    token = args.token

    if args.environments:
        invoke_method(token,
                      uri="environments/",
                      method='GET',
                      task=None)


if __name__ == '__main__':

    main()
