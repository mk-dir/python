str="We are learning how to program in python. python, python, python2 I find python programming fun"

#print(str.count("python"))
"""
f=open('hello File','w')
f.write(str)
f.close()
"""

"""f=open('hello File')
text=f.read()

print(text)"""
for line in open('hello File'): print(line)