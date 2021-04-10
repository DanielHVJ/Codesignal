def centuryFromYear(year):
    cen = 0
    cen = (year + 99)//100
    return cen


def checkPalindrome(inputString):
    return inputString == inputString[::-1]
    
    if checkPalindrome(inputString):
        print("true")
    else:
        print("false")

def adjacentElementsProduct(inputArray):
    l = len(inputArray) 
    sum = []
    for i in range(l-1):
        sum.append(inputArray[i] * inputArray[i+1]) 
        print(sum)
    return max(sum)

adjacentElementsProduct([3, 6, -2, -5, 7, 3])

def shapeArea(n):
    if n == 1:
        return 1
    area = (n*n) + ((n-1)*(n-1))
    return area

shapeArea(2)

def makeArrayConsecutive2(statues):
    return (max(statues)-min(statues)+1)-len(statues)

makeArrayConsecutive2([2,3,8,4])


def almostIncreasingSequence(sequence):
    removed_one = False
    prev_maxval = None
    maxval = None
    for i in sequence:
        if not maxval or i > maxval:
            prev_maxval = maxval
            maxval = i
        elif not prev_maxval or i > prev_maxval:
            if removed_one:
                return False
            removed_one = True
            maxval = i
        else:
            if removed_one:
                return False
            removed_one = True
    return True


def matrixElementsSum(matrix):
    sum_matrix = 0
    haunted_room = list()
    for i in range(0, len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                haunted_room.append(j)
                print(haunted_room)
        for k in range(len(matrix)):
            if k not in haunted_room:
                sum_matrix += matrix[i][k]
    return sum_matrix


matrix =[[1, 1, 1, 0], 
        [0, 5, 0, 2], 
        [2, 1, 0, 2]]

matrixElementsSum(matrix)

summ = 0
for i in range(len(matrix)):
    for k in range(0,2):
            summ += matrix[i][k]
print(summ)              


def allLongestStrings(inputArray):
    maxLen = 0
    for i in range(0,len(inputArray)):
        maxLen = max(maxLen,len(inputArray[i]))
    
    return [i for i in inputArray if len(i)==maxLen]

inputArray = ["aba", "aa", "ad", "vcd", "aba"]
allLongestStrings(inputArray)


#-----------
def common_character_count(str1: str, str2: str):
    str1_set = set(str2)
    result = 0
    for letter in str1_set:
        str1_count = str1.count(letter)
        str2_count = str2.count(letter)
        result += min([str1_count, str2_count])
    return result

s1 = "aabcc"
s2 = "adcaa"

print(common_character_count(s1, s2))

## IS LUCKY

def isLucky(n):
    s = str(n)
    first, second = s[:len(s)//2], s[len(s)//2:]
    first = sum(map(int, list(first)))
    second = sum(map(int, list(second)))
    return first == second

n = 1230
print(isLucky(n))

## -- SORT BY HEIGHT
def sortByHeight(a):
    b = sorted([i for i in a if i!=-1])
    j = 0
    for i in range(len(a)):
        if a[i] == -1:
            pass
        else:
            a[i]=b[j]
            j+=1
    return a

a = [-1, 150, 190, 170, -1, -1, 160, 180]
sortByHeight(a)

## ------------ REVERSE IN PARENTHESES
import re
def reverseParentheses(s):
    while "(" in s:
        match = re.search('\([^()]*\)', s)
        match_string = match.group(0)[1: len(match.group(0)) - 1]
        reversed_match_string = match_string[::-1]
        s = s[:match.start()] + reversed_match_string + s[match.end():]
    return s

a = "foo(bar)baz"    
b = "foo(bar)baz(blim)"

reverseParentheses(a)
reverseParentheses(b)

## 

def alternatingSums(a):
    res = ()
    if len(a) == 1:
        res = [a,0]
    else:
        res = [sum(a[i : : 2]) for i in range(len(a)//(len(a)//2))]
    return res

def alternatingSums2(a):
    return [sum(a[::2]),sum(a[1::2])]

alternatingSums(b)
a = [150,10,40,0]
b= [190]

## ADD A BORDER

def addBorder(picture):
    output = []
    border = ""
    for i in range(0,len(picture[0])+2):
        border += "*"
    output.append(border)
    for i in range(0,len(picture)):
        output.append("*"+picture[i]+"*")
    
    output.append(border)
    
    return output

picture = ["abc",
            "ded"]
addBorder(picture)

## ARE SIMILAR

def areSimilar(a, b):
    count = 0
    list_a = []
    list_b = []
    for i in range(len(a)):
        if (a[i]!= b[i]):
            count +=1
            list_a.append(a[i])
            list_b.append(b[i])

    if (count ==0):
        return True 
    elif count ==2: 
        return set(list_a)==set(list_b)
    else:
        return False

a = [1, 2, 3,5]
b = [2, 1, 3,6]

## ARRAY CHANGE
def arrayChange(inputArray):
    sum = 0
    q = inputArray[0]
    for i in inputArray[1:]:
        if i <= q:
            sum += q-i+1
            q = q+1
        else:
            q = i
    return sum

areSimilar(a,b)

## REARRANGING

def palindromeRearranging(inputString):
    char_occur = {} 
    
    for inp in inputString:
        if inp not in char_occur:
            char_occur[inp] = 1
        else:
            char_occur[inp] += 1

    odd_occ = [las for las in char_occur if char_occur[las] % 2]
    if len(odd_occ) > 1:
        return False
    else:
        return True
    
inputString = "aabb"
palindromeRearranging(inputString)

## EQUALLY STRONG
def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    return max(yourLeft, yourRight) == max(friendsLeft, friendsRight) and min(yourLeft, yourRight) == min(friendsLeft, friendsRight)

areEquallyStrong(15,10,15,10)

## find the maximal absolute difference between any two of its adjacent elements.

def arrayMaximalAdjacentDifference(a):
    diffs=[abs(a[i]-a[i+1]) for i in range(len(a)-1)]
    return max(diffs)


## Check IP address

def isIPv4Address(inputString):
    l = inputString.split('.')
    if len(l) != 4:
        return False
    for i in range(len(l)):
        if not l[i].isnumeric():
            return False
        elif (len(l[i]) > 1) and (l[i][0] == '0'):
            return False
        elif int(l[i]) not in range(256):
            return False
    return True

## AVOID OBSTACLES

def avoidObstacles(inputArray):
    for i in range(2, max(inputArray)):
        quantity = 0
        for x in inputArray:
            if x % i == 0:
                break
            quantity +=1
        if quantity == len(inputArray):
            return i
    return max(inputArray) + 1


def boxBlur(image):

#empty array to place values within the 3x3 matrix
  threeByThreeVals = []
#empty array to place the average of values within 3x3 matrix
  threeByThreeAvgs = []
#empty array to place average values into a matrix
  blurredMatrix = []

  #find the values of elements within all 3x3 matrixes and place in threeByThreeVals list
  #start loops at 1 and stop at one before the length's end since no elements at the ends 
  #can be the center of a 3x3 matrix
  for i in range(1, len(image) - 1):
    for j in range(1, len(image[i]) - 1):
      threeByThreeVals.append(
        #determine values within 3x3 matrixes with image[i][j] at center
        [image[i - 1][j - 1], image[i - 1][j], image[i - 1][j + 1],
         image[i][j - 1], image[i][j], image[i][j + 1],
         image[i + 1][j - 1], image[i + 1][j], image[i + 1][j + 1]])

  #calculate averages of 3x3 matrixes, round down to the nearest integer, and add them 
  #into threeByThreeAvgs list
  for i in range(len(threeByThreeVals)):
    threeByThreeAvgs.append(int(sum(threeByThreeVals[i]) / len(threeByThreeVals[i])))

  # A for loop goes from 0 to the length of the threeByThreeAvgs list, each iteration increases i 
  # by the length of image[0] - 2, which is the length of blurredMartix[x] that I want. This way when 
  # the list is sliced using i for the beginning of the slice it starts on the correct location and and 
  # i + image[0] - 2 ends the slice at the correct length.

  for i in range(0, len(threeByThreeAvgs), (len(image[0]) - 2)):
    blurredMatrix.append(threeByThreeAvgs[i:i + (len(image[0]) - 2)])

  #return blurred matrix
  return blurredMatrix

image=[[1,1,1],  [1,7,1],  [1,1,1]]

boxBlur(image) 


def neighbors(matrix,i,j,row,col):
    mine = 0
    if not ((i < 1) or (j < 1)):
        if matrix[i - 1][j - 1]:
            mine+=1
    if not (i < 1):
        if matrix[i - 1][j]:
            mine+=1
    if not ((i < 1) or (j >= col-1)):
        if matrix[i - 1][j + 1]:
            mine+=1
    if not (j >= col-1):
        if matrix[i][j + 1]:
            mine+=1
    if not ((i >= row-1) or (j >= col-1)):
        if matrix[i + 1][j + 1]:
            mine+=1
    if not (i >= row-1):
        if matrix[i + 1][j]:
            mine+=1
    if not ((i >= row-1) or (j < 1)):
        if matrix[i + 1][j - 1]:
            mine+=1
    if not (j < 1):
        if matrix[i][j - 1]:
            mine+=1
    return mine
            
def minesweeper(matrix):
    row = len(matrix)
    col = len(matrix[0])
    sol = []
    for i in range(0,row):
        temp = []
        for j in range(0,col):
            temp.append(neighbors(matrix,i,j,row,col))
        sol.append(temp)
    
    return sol


