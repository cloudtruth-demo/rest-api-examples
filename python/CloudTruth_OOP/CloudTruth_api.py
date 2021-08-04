#!/usr/bin/env python3
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
'''
CloudTruth REST module
'''

import logging
import requests


logger = logging.getLogger(__name__)


class CloudTruth():
    '''Base class'''

    def __init__(self, token):
        '''Instantiate a generic connection instance'''

        self.base_uri = 'https://api.cloudtruth.io/api/v1'
        self.headers = {'Authorization': f'API-Key { token }'}

    def operation(self, verb, url):
        response = requests.request(verb, url, headers=self.headers)
        return response

    def get_audit(self):
        '''Invoke Audit GET method'''
        request = self.operation('get', url=f'{self.base_uri}/audit/')
        return request.json()

    def get_audit_summary(self):
        '''Invoke Audit GET method'''
        request = self.operation('get', url=f'{self.base_uri}/audit/summary/')
        return request.json()

    def get_environments(self):
        '''Invoke Environment GET method'''
        request = self.operation('get', url=f'{self.base_uri}/environments/')
        return request.json()

    def get_aws(self):
        '''Invoke aws GET method'''
        request = self.operation('get',
                                 url=f'{self.base_uri}/integrations/aws/')
        return request.json()

    def get_github(self):
        '''Invoke github GET method'''
        request = self.operation('get',
                                 url=f'{self.base_uri}/integrations/github/')
        return request.json()

    def get_explore(self):
        '''Invoke explore GET method'''
        request = self.operation('get',
                                 url=f'{self.base_uri}/integrations/explore/')
        return request.json()

    def get_invitations(self):
        '''Invoke invitations GET method'''
        request = self.operation('get', url=f'{self.base_uri}/invitations/')
        return request.json()

    def get_memberships(self):
        '''Invoke memberships GET method'''
        request = self.operation('get', url=f'{self.base_uri}/memberships/')
        return request.json()

    def get_organizations(self):
        '''Invoke organizations GET method'''
        request = self.operation('get', url=f'{self.base_uri}/organizations/')
        return request.json()

    def get_projects(self):
        '''Invoke projects GET method'''
        request = self.operation('get', url=f'{self.base_uri}/projects/')
        return request.json()

    def get_serviceaccounts(self):
        '''Invoke service accounts GET method'''
        request = self.operation('get',
                                 url=f'{self.base_uri}/serviceaccounts/')
        return request.json()

    def get_users(self):
        '''Invoke users GET method'''
        request = self.operation('get', url=f'{self.base_uri}/users/')
        return request.json()
