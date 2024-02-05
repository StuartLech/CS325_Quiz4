import argparse

parser = argparse.ArgumentParser(description='Process a string, an integer, and a float.')

parser.add_argument('string', type=str, help='A string argument')
parser.add_argument('integer', type=int, help='An integer argument')
parser.add_argument('float', type=float, help='A float argument')

args = parser.parse_args()

print(f"String argument: {args.string}")
print(f"Integer argument: {args.integer}")
print(f"Float argument: {args.float}")
