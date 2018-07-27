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

import os
import sys
import json
import logging
import config
from collections import defaultdict
from utils import configurator
from zaqarclient.queues.v1 import client

LOG = logging.getLogger(__name__)

class Zaqar(object):
	def __init__(self, conf):
		if conf is not None:
			self.config = conf
		'''
		LOG.debug(self.config.os_auth_url)
		LOG.debug(self.config.clientuuid)
		LOG.debug(self.config.os_project_name)
		LOG.debug(self.config.os_project_id)
		LOG.debug(self.config.zaqar_endpoint)
		'''
		self.zqc = client.Client(self.config.zaqar_endpoint, conf={
			'auth_opts': {
				'options': self.config.zaqar_conf
			}
		}, version=2)


	def get_message(self, qname, gr, t):
		q = self.zqc.queue(qname)
		claim = q.claim(ttl=t, grace=gr)  # bug #1553387
		[print(msg.body) for msg in claim]


	def send_message(self, qname, msg):
		q = self.zqc.queue(qname)
		q.post([{'body': msg}])



if __name__ == '__main__':

	c = configurator.Configurator(config)

	zq = Zaqar(conf=c)
	zq.send_message("foobar", "HELLO ZAQAR >>>")
	zq.get_message("foobar", 600, 600)
