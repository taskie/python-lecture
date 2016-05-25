import argparse

parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()
group.add_argument('-H', "--head", metavar='n', type=int, help="head")
group.add_argument('-T', "--tail", metavar='n', type=int, help="tail")
parser.add_argument("-t", "--tac", action="store_true", help='tac')
parser.add_argument('-u', "--uniq", action="store_true", help="uniq")
parser.add_argument('file', nargs='*', type=argparse.FileType('r'))

args = parser.parse_args()
print(args)
