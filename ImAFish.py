#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# ImAFish
#
# ImAFish is a simple python script to help hackers fill their phishing
#     databases. It is a fun project to send http POST requests using pythons
#     requests library. It can be used to automatically and semi-randomly fill
#     out login forms of phishing sites.
#
# https://github.com/Andreas-Menzel/ImAFish
#-------------------------------------------------------------------------------
# @author: Andreas Menzel
# @license: MIT License
# @copyright: Copyright (c) 2022 Andreas Menzel
#-------------------------------------------------------------------------------


import argparse
from random import choice, random
import requests
from time import sleep


def check_positive(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
    return ivalue

def check_not_negative(value):
    ivalue = int(value)
    if ivalue < 0:
        raise argparse.ArgumentTypeError("%s is an invalid non-negative int value" % value)
    return ivalue

# Setup argument parser
prog_epilog = 'FIXED PARAMETER' + '\n'
prog_epilog += 'Uses a fixed value for a parameter.' + '\n'
prog_epilog += 'usage:\t\t--param <name>#<value>' + '\n'
prog_epilog += 'example:\t--param user#superuser' + '\n\n'

prog_epilog += 'RANDOM STRING PARAMETER' + '\n'
prog_epilog += 'Generates a random string for a parameter.' + '\n'
prog_epilog += 'usage:\t\t--param_random_str <name>#<min_len>#<max_len>#<chars>' + '\n'
prog_epilog += 'example:\t--param_random_str password#8#12#abcdef123' + '\n\n'

prog_epilog += 'RANDOM ELEMENT PARAMETER' + '\n'
prog_epilog += 'Choses a random element from a list as the value for a parameter.' + '\n'
prog_epilog += 'usage:\t\t--param_random_elem <name>#<value0>#<value1>#...' + '\n'
prog_epilog += 'example:\t--param_random_elem website#example.com#example.net' + '\n\n'

prog_epilog += 'RANDOM FILE ELEMENT PARAMETER' + '\n'
prog_epilog += 'Choses a random element from a list of a file as the value for a parameter.' + '\n'
prog_epilog += 'usage:\t\t--param_random_file_elem <name>#<filename>' + '\n'
prog_epilog += 'example:\t--param_random_file_elem password#passList.txt' + '\n\n'

parser = argparse.ArgumentParser(description='', epilog=prog_epilog, prog='ImAFish', formatter_class=argparse.RawDescriptionHelpFormatter,)
parser.add_argument('--url',
    help='The URL.')
parser.add_argument('--runs',
    type=check_positive,
    default=1,
    help='Number of runs.')
parser.add_argument('--delay',
    type=check_not_negative,
    default=1,
    help='Delay in seconds between each run.')
parser.add_argument('-v', '--verbose',
    action='store_true',
    help='Print more information')
parser.add_argument('--param',
    nargs='*',
    help='Fixed parameter.')
parser.add_argument('--param_random_str',
    nargs='*',
    help='Random string parameter.')
parser.add_argument('--param_random_elem',
    nargs='*',
    help='Random element parameter.')
parser.add_argument('--param_random_file_elem',
    nargs='*',
    help='Random element from file parameter.')
args = parser.parse_args()


def random_string(min_len, max_len, chars):
    length = round(random() * (max_len - min_len) + min_len)
    random_string = ''
    for i in range(0, length):
        random_string += chars[round(random() * len(chars) - 1)]
    return random_string


for i in range(1,args.runs + 1):
    parameters = {}

    # param
    if not args.param == None:
        for elem in args.param:
            parameter = elem.split('#')
            key = parameter[0]
            value = parameter[1]
            parameters[key] = value

    # param_random_str
    if not args.param_random_str == None:
        for elem in args.param_random_str:
            parameter = elem.split('#')
            key = parameter[0]
            value = random_string(int(parameter[1]), int(parameter[2]), parameter[3])
            parameters[key] = value

    # param_random_elem
    if not args.param_random_elem == None:
        for elem in args.param_random_elem:
            parameter = elem.split('#')
            key = parameter[0]
            value = choice(parameter[1:])
            parameters[key] = value

    # param_random_file_elem
    if not args.param_random_file_elem == None:
        for elem in args.param_random_file_elem:
            parameter = elem.split('#')
            key = parameter[0]
            with open(parameter[1]) as file:
                # take random line and remove '\n'
                value = choice(list(file))[0:-1]
            parameters[key] = value

    if args.verbose:
        print('Sending request no.', i, 'with parameters', parameters)
    else:
        print('Sending request no.', i)
    request = requests.post(args.url, parameters)

    if i < args.runs:
        if args.delay > 0:
        	sleep(args.delay)
