path = "/Users/apple/Downloads/2021-05-25.txt"
a = [
{"yoyo1": "123456"},
{"yoyo2": "123456"},
{"yoyo3": "123456"},
]
with open(path,'w+') as f:
    for i in a:

        #f.write(str(i))
        #print(type(i))
        #print(i)
        for k,y in i.items():
            aa = k+","+y+'\n'
            f.write(aa)

            print(k,y)
            print(type(k))


print(f)