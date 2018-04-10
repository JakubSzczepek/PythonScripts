from pprint import pprint

FILE = r"D:\PythonProject\host.txt"
output = []

with open(FILE) as file:
  for line in file.readlines():
      if not line.isspace() and not line.startswith('#'):
          ip, *hostnames = line.split()
          output.append({'ip': ip,
                'hostnames': hostnames,
                'protocol': 'ipv4' if '.' in ip else 'ipv6'})

pprint(output)