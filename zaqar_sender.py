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
from collections import defaultdict
from zaqarclient.queues.v1 import client

#logging.basicConfig(filename='/tmp/zaqar.log', level=logging.DEBUGGING)


class Zaqar(object):
	def __init__(self, conf):

		#print(json.dumps(conf, indent=2))

		self.zqc = client.Client('http://10.3.168.102:8888', conf={
			'auth_opts': {
				'options': conf
			}
		}, version=2)


	def send_message(self, qname, msg):
		q = self.zqc.queue(qname)
		q.post([{'body': msg}])



if __name__ == '__main__':
	conf = defaultdict()
	conf.__setitem__('client_uuid', "7288873d-f73a-473b-ae36-96a2246fd61a")
	conf.__setitem__('os_auth_token', "gAAAAABbKnz_daD2CAXUCk1Vyu8e7LbS-vmX2LQo_v366y22A5mnr-lCGJ3SXGatyJpIprq3Wu6jeTVQ8OEjzR2DiY0bv_dSv-Cc4euTBKc3ZI21FBZM0NmmprgOxrJ8wg8OOLVdOYr9u1Ehbo9WOz47-UW2c0bw86lVTptCKSFZDdbQArVYZ-0")
	conf.__setitem__('os_auth_url', 'http://10.3.168.24:35357/v3')
	conf.__setitem__('os_project_id', '78b6573f19884f86a5a6ca607dcf178e')

	zq = Zaqar(conf)
	zq.send_message("foobar", "HELLO ZAQAR >>>")
