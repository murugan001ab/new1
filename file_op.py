#file1=open('filename','mood')
"""
moods
read r
write w
append a
"""
file1=open('text','r')
file2=open('text1.txt','a+')
for lines in file1:
    file2.write(lines)
file1.close()
file2.close()
