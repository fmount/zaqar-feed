#!/usr/bin/env python

#######################################################################
#
#	 Licensed under the Apache License, Version 2.0 (the "License");
#	 you may not use this file except in compliance with the License.
#	 You may obtain a copy of the License at
#
#		 http://www.apache.org/licenses/LICENSE-2.0
#
#	 Unless required by applicable law or agreed to in writing, software
#	 distributed under the License is distributed on an "AS IS" BASIS,
#	 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#	 See the License for the specific language governing permissions and
#	 limitations under the License.
#
#	 author: fpantano <francesco.pantano@fastweb.it>
#	 version: 0.1
#	 company: Fastweb S.p.a.
#
########################################################################


from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client
from prettytable import PrettyTable
from utils.user import User
from keystoneclient.v3.tokens import TokenManager


class Wkeystone():

	# Just to make sure there is only one client
	__instance = None

	def __init__(self, u, debug=False):
		
		if Wkeystone.__instance:
			raise Exception("Just one client per session allowed!")
		
		Wkeystone.__instance = self
		
		self.user = u
		self.debug = debug

		#print('-'.join((u.project_id, u.domain_id)))

		auth = v3.Password(username=u.name, \
				password=u.password, \
				project_id=u.project_id, \
				user_domain_id=u.domain_id, \
				auth_url=u.endpoint)
		
		self.s = session.Session(auth=auth)
		self.keystone = client.Client(session=self.s)


	def __str__(self):
		print(self.keystone)


	def saysomething(self):
		print("I exist and I'm alone ...")


	def new_token(self):
		return self.s.get_timings()


	def tenant_list(self):
		tlist = []
		[tlist.append(tenant.id) for tenant in self.keystone.projects.list()]
		return tlist


	def print_tenant_list(self):
		x = PrettyTable(['Tenant ID', 'Tenant Name', 'Is Private IaaS', 'Enabled'])
		for tenant in self.keystone.projects.list():
			x.add_row([tenant.id, tenant.name, getattr(tenant, 'private_iaas', False), tenant.enabled])
		print(x)


	def validate_token(self, token):
		mgr = TokenManager(self.keystone)
		mgr.validate(token, include_catalog=False, allow_expired=False)

	def tenant_name_to_uuid(self, tname):
		'''
		Return the uuid of the FIRST occurrence of the tenant name matched
		'''
		for tenant in self.keystone.tenants.list():
			if(tenant.name == tname):
				return tenant.id


	def tenant_to_name(self, tid):
		'''
		Print the name of the provided tenant id
		'''
		#return [ name if tid == tenant.name for tenant in self.keystone.tenants.list()]
		#list(filter(lambda x: x == tid, (self.keystone.tenants.list())))
		for tenant in self.keystone.tenants.list():
			if(tenant.id == tid):
				return tenant.name


	def uid_to_name(self, uid):

		for user in self.keystone.users.list():
			if(user.id == uid):
				return user.name
