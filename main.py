def transform(b):
    for i in range(len(b)-1):
        if b[i] == '1':
            b[i] = '0'
            if b[i+1] == '0':
                b[i+1] = '1'
            else:
                b[i+1] = '0'
    return b

if __name__ == "__main__":
    a = list("01111100000111111110111000")
    print(a)
    while a != transform(list(a)):
        a = transform(list(a))
    print(a)
