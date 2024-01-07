def split_and_join(line):
    # write your code here
    line=line.split("")
    str=""
    for x in line:
        str+=-x
    return str

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
