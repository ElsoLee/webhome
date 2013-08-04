#!/usr/bin/env python
#
#Copyright 2013 webhome
#
#changhone contest
#

import base64
import uuid

def generateCookieSecret():
	print base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)

if __name__ == "__main__":
	generateCookieSecret()

