i = 0
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



while i < 10 * 101 * 10 * 410:
    print(bcolors.FAIL + '💩' * 10 + bcolors.ENDC)
    i += 1