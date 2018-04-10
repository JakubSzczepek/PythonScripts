import datetime
from pprint import pprint

DISABLED_SHADOW_ENTRY = {'!', '!!', '*'}

FILE1 = r"D:\PythonProject\pass.txt"
FILE2 = r"D:\PythonProject\shadow.txt"
FILE3 = r"D:\PythonProject\group.txt"

users = []

ALGORITHMS ={
       '$1$:': 'MD5',
       '$2a$': 'Blowfish',
       '$2y$': 'Blowfish',
       '$5$': 'SHA-256',
       '$6$': 'SHA-512'
}

with open(FILE1) as passwd, \
        open(FILE2) as shadow, \
        open(FILE3) as group:

        etc_passwd = passwd.readlines()
        etc_shadow = shadow.readlines()
        etc_group = group.readlines()

for line in etc_passwd:
    if not line.isspace() and not line.startswith('#'):
        login, _, uid, gid, gecos, home, shell = line.strip().split(':')

        if int(uid) < 1000:
            continue

        groups = []
        algorithm = None
        password = None
        lastchanged = 0
        locked = False

        for line in etc_group:
            if not line.isspace() and not line.startswith('#'):
                gr_name, gr_passwd, gr_gid, gr_members = line.strip().split(':')
                if login in gr_members.split(','):
                    groups.append(gr_name)

        for line in etc_shadow:
            if not line.isspace() and not line.startswith('#'):
                sh_login, sh_password, sh_lastchanged, *_ = line.strip().split(':')

                if sh_login != login:
                    continue

                sh_lastchanged = int(sh_lastchanged) * 60 * 60 * 24
                lastchanged = datetime.date.fromtimestamp(sh_lastchanged)

                if sh_password in DISABLED_SHADOW_ENTRY:
                    locked = True
                    break

                for string in ALGORITHMS.keys():
                    if sh_password.startswith(string):
                        algorithm = ALGORITHMS.get(string)
                        password = sh_password.replace(string, '')

        users.append({
                'login': login,
                'uid': uid,
                'gid': gid,
                'home': home,
                'shell': shell,
                'algorithm': algorithm,
                'password': password,
                'groups': groups,
                'lastchanged': lastchanged,
                'locked': locked,
            }
        )

pprint(users)