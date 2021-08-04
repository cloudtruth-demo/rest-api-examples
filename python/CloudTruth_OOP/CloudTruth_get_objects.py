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
'''
Returns specified organization object json
'''

import argparse
import getpass
import json
import requests
import CloudTruth_api

# Disable SSL warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def parse_args():
    '''Parse command line arguments'''

    parser = argparse.ArgumentParser()

    parser.add_argument('-t', '--token',
                        required=False,
                        help="Specify the API Acces Token")

    parser.add_argument('-a', '--audit',
                        action='store_true',
                        required=False,
                        help="Get Audit")

    parser.add_argument('-as', '--auditsum',
                        action='store_true',
                        required=False,
                        help="Get Audit summary")

    parser.add_argument('-e', '--environments',
                        action='store_true',
                        required=False,
                        help="Get environments")

    parser.add_argument('-z', '--aws',
                        action='store_true',
                        required=False,
                        help="Get AWS Integrations")

    parser.add_argument('-g', '--github',
                        action='store_true',
                        required=False,
                        help="Explore Integrations")

    parser.add_argument('-x', '--explore',
                        action='store_true',
                        required=False,
                        help="Get GitHub Integrations")

    parser.add_argument('-i', '--invitations',
                        action='store_true',
                        required=False,
                        help="Get Invitations")

    parser.add_argument('-m', '--memberships',
                        action='store_true',
                        required=False,
                        help="Get Memberships")

    parser.add_argument('-o', '--organizations',
                        action='store_true',
                        required=False,
                        help="Get Orgnizations")

    parser.add_argument('-p', '--projects',
                        action='store_true',
                        required=False,
                        help="Get Projects")

    parser.add_argument('-s', '--apiaccounts',
                        action='store_true',
                        required=False,
                        help="Get API access tokens accounts")

    parser.add_argument('-u', '--users',
                        action='store_true',
                        required=False,
                        help="Get users")

    args = parser.parse_args()

    if not args.token:
        args.token = getpass.getpass(("Please enter your API Access Token: "))
    return args


def main():
    '''Main'''

    args = parse_args()
    token = args.token
    CloudTruth = CloudTruth_api.CloudTruth(token)

    if args.audit:
        audit = CloudTruth.get_audit()
        print(json.dumps(audit, indent=4, sort_keys=True))

    if args.auditsum:
        audit_summary = CloudTruth.get_audit_summary()
        print(json.dumps(audit_summary, indent=4, sort_keys=True))

    if args.environments:
        environments = CloudTruth.get_environments()
        print(json.dumps(environments, indent=4, sort_keys=True))

    if args.aws:
        aws = CloudTruth.get_aws()
        print(json.dumps(aws, indent=4, sort_keys=True))

    if args.github:
        github = CloudTruth.get_github()
        print(json.dumps(github, indent=4, sort_keys=True))

    if args.explore:
        explore = CloudTruth.get_explore()
        print(json.dumps(explore, indent=4, sort_keys=True))

    if args.invitations:
        invitations = CloudTruth.get_invitations()
        print(json.dumps(invitations, indent=4, sort_keys=True))

    if args.memberships:
        memberships = CloudTruth.get_memberships()
        print(json.dumps(memberships, indent=4, sort_keys=True))

    if args.projects:
        projects = CloudTruth.get_projects()
        print(json.dumps(projects, indent=4, sort_keys=True))

    if args.organizations:
        organizations = CloudTruth.get_organizations()
        print(json.dumps(organizations, indent=4, sort_keys=True))

    if args.apiaccounts:
        apiaccounts = CloudTruth.get_serviceaccounts()
        print(json.dumps(apiaccounts, indent=4, sort_keys=True))

    if args.users:
        users = CloudTruth.get_users()
        print(json.dumps(users, indent=4, sort_keys=True))


if __name__ == '__main__':

    main()
