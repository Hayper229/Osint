#!/bin/python3

import whois
import sys
dom=sys.argv[1]
whois_info=whois.whois(dom)

print(whois_info)

