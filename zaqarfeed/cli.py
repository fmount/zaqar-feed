#! /usr/bin/env python

#######################################################################
#
#	 Licensed under the Apache License, Version 2.0 (the "License");
#	 you may not use this file except in compliance with the License.
#	 You may obtain a copy of the License at
#
#	 http://www.apache.org/licenses/LICENSE-2.0
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


from wkeystone import Wkeystone as kclient
from utils.user import User
from collections import defaultdict, Counter
import os
import re
import sys
import json
import optparse
import logging
from prettytable import PrettyTable

#TODO:
# 1. Put this supported versions in a conf file :/
# 2. Define better the debug level and the file used
# 3.
#

SUPPORTED_API_VERSIONS = [2, 3]

logging.basicConfig(filename='/tmp/zaqar_cli.log', level=logging.DEBUG)
LOG = logging.getLogger(__name__)


def read_keystonerc(ksrc):
	prms = defaultdict()
	with open(ksrc, 'r') as f:
		for line in f:
			if(line.startswith("export")):
				item = re.sub('export', '', line)
				#print(' - '.join((l.split('=')[0].lstrip(), l.split('=')[1])))
				prms.__setitem__(item.split("=")[0].lstrip(), item.split("=")[1].rstrip())
	return prms


def read_env(parser):
	
	if(os.getenv('OS_USERNAME') is None) or \
		(os.getenv('OS_PASSWORD') is None) or \
		(os.getenv('OS_TENANT_NAME') is None) or \
		(os.getenv('OS_AUTH_URL') is None):
			print(parser.usage)
			exit(-1)
	prms = defaultdict()
	prms.__setitem__('OS_USERNAME', os.getenv('OS_USERNAME', 'None'))
	prms.__setitem__('OS_TENANT_NAME', os.getenv('OS_TENANT_NAME', 'None'))
	prms.__setitem__('OS_PASSWORD', os.getenv('OS_PASSWORD', 'None'))
	prms.__setitem__('OS_AUTH_URL', os.getenv('OS_AUTH_URL', 'None'))
	
	return prms


def init(*args):
	dic = defaultdict()
	dic.__setitem__('kclient', kclient(User(args[0])))
	return dic


def cli():
	print("------------------------------")
	print("ZAQAR CLI PLUGIN")
	print("------------------------------\n")

	parser = optparse.OptionParser('\nsource keystonerc* \nusage %prog -f tenant_file')
	parser.add_option('-f', dest='tenant_file', type='string', help='tenant file to authenticate on keystone')
	parser.add_option('--debug', action='store_true', dest='debug', help='activate DEBUG MODE to print all critical statement during the algorithm execution')

	(options, args) = parser.parse_args()

	tenant_file = options.tenant_file
	debug = options.debug

	if tenant_file is None:
		LOG.info("[I] Read user info from ENV")
		params = read_env(parser)
	else:
		LOG.info("[I] Loading keystonerc")
		params = read_keystonerc(tenant_file)

	clients = init(params)
	wk = clients['kclient']
	wk.print_tenant_list()


if __name__ == '__main__':
	cli()
