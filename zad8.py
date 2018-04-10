from pprint import pprint

FILE1 = r"D:\PythonProject\pass.txt"
FILE2 = r"D:\PythonProject\shadow.txt"
FILE3 = r"D:\PythonProject\group.txt"

output = []
name_2 = []
with open(FILE1) as file1, \
        open(FILE2) as file2, \
        open(FILE3) as file3:
    for line in file1.readlines():
        if not line.isspace() and not line.startswith('#'):
            user, _, uid, gid, name, directory, shell = line.strip('\n').split(':')
            if int(uid) > 1000:
                for line in file2.readlines():
                    if not line.isspace() and not line.startswith('#'):
                        user2, algorithm, _, _, _, _, _, _, _ = line.strip('\n').split(':')
                        print(user)
                        if user in user2:
                            for line in file3.readlines():
                                if not line.isspace() and not line.startswith('#'):
                                    name, gdi2, _, *members = line.strip('\n').split(':')
                                    members = members[0].split(',')
                                    if user in members:
                                        name_2.append(name)
                                    output.append({'login': user,
                                                   'uid': uid,
                                                   'gid': gid,
                                                   'directory': directory,
                                                   'shell': shell,
                                                   'algorithm':
                                                       'SHA-256' if algorithm.startswith(
                                                       '$5$') else 'SHA-256',
                                                   'password:': algorithm[3:-1],
                                                   'goups': name_2
                                                   })

# pprint(output)

# if int(uid) > 1000:

#                     })
