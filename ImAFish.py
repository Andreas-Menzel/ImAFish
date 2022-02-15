import argparse
from random import random
import requests

# Setup argument parser
parser = argparse.ArgumentParser(description='', prog='ImAFish')
parser.add_argument('--url',
    help='The URL.')
parser.add_argument('--param',
    nargs='*',
    help='Fixed parameters.')
parser.add_argument('--param_random',
    nargs='*',
    help='Sends parameter. Generates random string.')
args = parser.parse_args()



def random_string(min_len, max_len, chars):
    length = round(random() * (max_len - min_len) + min_len)
    random_string = ''
    for i in range(0, length):
        random_string += chars[round(random() * len(chars) - 1)]
    return random_string



parameters = {}

# param
if not args.param == None:
    for elem in args.param:
        parameter = elem.split('#')
        key = parameter[0]
        value = parameter[1]
        parameters[key] = value

# param_random
if not args.param_random == None:
    for elem in args.param_random:
        parameter = elem.split('#')
        key = parameter[0]
        value = random_string(int(parameter[1]), int(parameter[2]), parameter[3])
        parameters[key] = value


request = requests.post(args.url, parameters)
print(request.text)
