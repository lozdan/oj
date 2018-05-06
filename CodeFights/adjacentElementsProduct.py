# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: adjacentElementsProduct
# problem url: https://codefights.com/arcade/intro/level-2/xzKiBHjhoinnpdh6m

def adjacentElementsProduct(inputArray):
    y = -1000
    for i in range (len (inputArray) - 1):
        if inputArray[i] * inputArray[i + 1] > y:
            y = inputArray[i] * inputArray[i + 1]
    return y

