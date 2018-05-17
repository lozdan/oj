# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: Base Conversion
# problem url: https://codefights.com/arcade/python-arcade/meet-python/u7FW6fpp8Mqxe6sjt

def baseConversion(n, x):
    return  hex(int(n, x))[2:]
