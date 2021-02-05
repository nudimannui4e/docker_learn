#!/usr/bin/env python3

import urllib.request

fp = urllib.request.urlopen("http://localhost:1234/")

encodedContent = fp.read()
decodedContent = encodedContent.decode("utf-8")

print(decodedContent)

fp.close()
