#!/usr/bin/env python

#######################################################################
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
#    author: fpantano <francesco.pantano@fastweb.it>
#    version: 0.1
#    company: Fastweb S.p.a.
#
########################################################################

from prettytable import PrettyTable
from collections import defaultdict
import re
import os


class User():

    def __init__(self, params):
        for key in params.keys():
            if params[key] == "None":
                raise Exception("[ERROR] Error Loading Parameters: check your keystonerc")
                return -1
        self.name = params.get('OS_USERNAME', 'None')
        self.password = params.get('OS_PASSWORD', 'None')
        self.tenant_name = params.get('OS_TENANT_NAME', 'None')
        self.project_id = params.get('OS_PROJECT_ID', 'None')
        self.domain_id = params.get('OS_DOMAIN_ID', 'None')
        self.endpoint = params.get('OS_AUTH_URL', 'None')
        '''
        Zaqar accepts the client_id as parameter to make ops on
        queues / topics. This parameter should exists in order
        to authenticate on Zaqar.
        '''
        self.client_id = params.get('OS_CLIENT_ID', 'None')
        self.api_version = "v3"


    def __str__(self):
        x = PrettyTable()
        x = PrettyTable(["Name", "Password", "Project", "Domain", "Endpoint", "API"])
        x.add_row([self.name, ''.join(['*' for _ in self.password]),\
            self.project_id, self.domain_id, self.endpoint, self.api_version])

        return str(x)
