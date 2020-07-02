# 1. Define a function which receives a string as a parameter. The function splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
# Examples:
# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']

def func1(strA):
    print('1. The string is: {}'.format(strA))
    strA = strA.replace(" ","")
    if len(strA) % 2 == 1:
        newstrA = strA + '_'
    else:
        newstrA = strA
    res = ','.join(newstrA[i:i + 2] for i in range(0, len(newstrA), 2))
    print('1. Result is: {}'.format(res))

a = 'ana cere mere'
b = func1(a)

c = 'ana are mere'
d = func1(c)

# 2. Create a function function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

def func2(strA):
    print('2. The string is: {}'.format(strA))
    strb = " "
    a = strA.split()
    newStrA = [x[::-1] for x in a]
    print('2. Result for problem 2: {}'.format(strb.join(newStrA)))

a = 'This is an example!'
func2(a)

c = 'double  spaces'
func2(c)

# 3. According to the creation myths of the Abrahamic religions, Adam and Eve were the first Humans to wander the Earth.
# You have to do God's job. The creation method must return an array of length 2 containing objects (representing Adam and Eve).' \
# The first object in the array should be an instance of the class Man. The second should be an instance of the class Woman.
# Both objects have to be subclasses of Human. Your job is to implement the Human, Man and Woman classes, then to define the creation
# function as stated above.

class Human:
    def __init__(self,name):
        self.name = name

    def _printName_(self):
        print(self.name)

class Man(Human):
    def __init__(self, name):
        Human.__init__(self,name)
    def _printManName_(self):
        print (self.name)

class Woman(Human):
    def __init__(self, name):
        Human.__init__(self,name)
    def _printWomanName_(self):
        print (self.name)

def func3():
    a = Man('Adam')
    a._printManName_()

    b = Woman('Eva')
    b._printWomanName_()

    retList = [a.name, b.name]
    print(retList)

func3()






