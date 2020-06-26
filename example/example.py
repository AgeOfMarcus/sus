import argparse

p = argparse.ArgumentParser()
p.add_argument("x", help=("YEP COCK"), required=False)
args = p.parse_args()

print("Hello, %s!" % (args.x or "world"))