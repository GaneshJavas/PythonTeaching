#! python3
from sys import argv
tool_name,file=argv

s=open(file).read(10)
a=0
v=0
c=0
for i in s:
    if i==" ":
        a=a+1
    elif i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        v=v+1
    elif i in ["!","@","#","$","%","^","&","*","(",")","_","-","=","+",",",".","/","<",">","]","["]:
        c=c+1
print("numer of space:",a)
print("total len:", len(str(s)))
print("number of vowels:", v)
print("special car.:",c)

# PS C:\PythonTeaching\tools> .\tools1.py ..\02_loops\Series\series2.py
# numer of space: 75
# total len: 257
# number of vowels: 36
# special car.: 43