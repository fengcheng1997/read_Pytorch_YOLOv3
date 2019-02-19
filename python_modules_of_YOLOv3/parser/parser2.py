import argparse

parser = argparse.ArgumentParser(description = 'this is a description')
parser.add_argument('--ver', '-v', action = 'store_true', help = 'hahaha')
# 将变量以标签-值的字典形式存入args字典
args = parser.parse_args()
if args.ver:
    print("Ture")
else:
    print("False")
    
# python parser2.py --ver 
