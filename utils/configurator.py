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
#	 author: fmount <fmount9@autistici.org>
#	 version: 0.1alpha
#	 company: --
#
########################################################################


#!/usr/bin/env python

import logging
from utils.parser import Parser

logging.basicConfig(filename='/tmp/zaqar.log', level=logging.DEBUG)
LOG = logging.getLogger(__name__)

class Configurator(Parser):

	def __init__(self, conf=None):
		super(Configurator, self).__init__(conf.parameters_json_file_source)

		self.parse()

	def __setattr__(self, key, value):
		self.__dict__[key] = value

	def parse(self):
		self.configure = self.raw_json
		for key, value in self.configure.get("global").items():
			if getattr(self, key, None) is None:
				setattr(self, key, value)
			LOG.debug("[CONFIGURATOR] Acquiring attribute [%s] with default value [%s]" % (key, str(value)))
		self.zaqar_conf = self.configure["global"]
		'''
		LOG.debug(self.keystone_endpoint)
		LOG.debug(self.projectname)
		LOG.debug(self.zaqar_conf)
		'''
