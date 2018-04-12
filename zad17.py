import sys


FILE1 = r"D:\PythonProject\pass.txt"

def read_conntent(file):
    login = []
    with open(FILE1) as file:
        for line in file.readlines():
            if not line.isspace() and not line.startswith('#'):
                user, _, uid, *_ = line.strip('\n').split(':')
                if int(uid) > 1000:
                  login.append(user)
    return login

def read_conntent2(file):
    with open(FILE1) as file:
        for line in file.readlines():
            if not line.isspace() and not line.startswith('#'):
                user, _, uid, *_ = line.strip('\n').split(':')
                if int(uid) > 1000:
                    yield user


output = read_conntent(FILE1)
output2 = [x for x in read_conntent2(FILE1)]

print(sys.getsizeof(output))
print(sys.getsizeof(output2))


output = read_conntent(FILE1)
output2 = read_conntent2(FILE1)

print(sys.getsizeof(output))
print(sys.getsizeof(output2))