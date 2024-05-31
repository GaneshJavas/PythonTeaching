# 2x2
a = [[1, 1],
     [2, 2]]
# 2x2
b = [[3, 3],
     [4, 4]]
c = []
def add(a, b):
    for i in range(2):
        temp=[]
        for j in range(2):
            temp.append(a[i][j] + b[i][j])
        c.append(temp) 

def subs(a, b):
    for i in range(2):
        temp=[]
        for j in range(2):
            temp.append(a[i][j] - b[i][j])
        c.append(temp) 

    for i in range(2):
            temp=[]
            for j in range(2):
                temp.append(a[i][j] + b[i][j])
            c.append(temp)
print(c)
