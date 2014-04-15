# if/else case1
sex = "f" 
if sex == "m": 
    print "Male" 
elif sex == "f": 
    print "Female" 
else: 
    print "Unknown"

# dictionary: switch/case 
sex = {"m":"Male", "f":"Female"} 
print sex.get("a", 'Unknown')

print '\n'

# case2
# method1
import platform 

if platform.system() == "Linux": 
    OS = "Linux" 
else: 
    OS = "Unknown" 
print OS
#method2: revise
OS = 'Linux' if platform.system() == "Linux" else 'Unknown'
print OS

print '\n'

# practice
a = "abc"
if a == "123": 
    ANS = "true" 
else: 
    ANS = "false" 
print ANS

ANS = 'true' if a == 'abc' else 'false'
print ANS


# judgement of two conditions ???

print '\n'

# for
LIST = ["ABC", 'xyz', 123] 
for L in LIST: 
    print L 

DICTIONARY = {"A":"ABC", 'b':"xyz", "0":123} 
for D in DICTIONARY.keys(): 
    print DICTIONARY[D] 

for A in range (5): 
    print A

# list comprehension ???

print '\n'

# while
#import sys 
#
#print "Input the word, [Quit]" 
#input = sys.stdin.readline().rstrip() 
#
#while input != "Quit": 
#    print "Your keyin: ", input 
#    input = sys.stdin.readline().rstrip()