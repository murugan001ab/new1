file1=open('text','r')
file2=open('text1.txt','a')
vow=['a','e','i','o','u','A','E','I','O','U']
for lines in file1:
    if lines[0] in vow:
        file2.write(lines)
file1.close()
file2.close()

