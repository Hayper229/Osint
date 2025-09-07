import requests
import socket
import whois
filename = "DUMP.html"
with open(f'{filename}', 'w') as f:
     f.write('<! DOCTYPE html>\n<html lang="en">\n<head>\n<title>\n  OSINT DUMP\n</title>\n  <meta charset="utf-8">\n</head>\n<body>\n<h2 class="maintext" style="text-align: center">INFO</h2>\n')

with open('test.txt', 'r') as f:
     save_one = f.read()
     subs = save_one.split()
     for sub in subs:
         ips = socket.gethostbyname(sub)
         ips_list = ips.split()
         who = whois.whois(sub)
         for ip in ips_list:
             with open(f'{filename}', 'a') as f:
                  f.write(f'<hr>\n<h3 class="inf">Subdomain: {sub}</h3>\n<h4 class="inf">IP: {ip}</h4>\n<h4 class="inf">WhoIs \n[<br>\nDomain_name: {who["domain_name"]}\n<br>\nRegistrar: {who["registrar"]}\n<br>\nCreation Date: {who["creation_date"]}\n<br>\nUpdated Date: {who["updated_date"]}\n<br>Expiration Date: {who["expiration_date"]}\n<br>Emails: {who["emails"]}\n<br>]\n</h4>')
                  pass

with open(f'{filename}', 'a') as f:
     f.write('<style>.inf {color: green; }\nbody {color: black; }\n.maintext {\ncolor: RED; }\n</style></body>\n</html>')
     print('Ending')
