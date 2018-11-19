i="_akshay@rosho.org"
x=i.split("@")[0]
c1=0
c2=0
c3=0
if ".com"in i or ".in" in i or ".edi" in i:
    if x.islower()==True:
        if len(x)>3:
            if "." in x or "-" in x or "_" in x:
                if "." not in x[:1] and "-" not in x[:1] and "_" not in x[:1] and "." not in x[-1:] and "-" not in x[-1:] and "_" not in x[-1:]:
                  print("Valid")
else:
    c1+=1
if len(x)<=3:
    c2+=1
if "." not in x and "-" not in x and "_" not in x:
    c3+=1
if "." in x[:1] or "-" in x[:1] or "_" in x[:1] or "." in x[-1:] or "-" in x[-1:] or "_" in x[-1:]:
    c3+=1
if((c1+c2+c3)>=1):
    print("Invalid")
    if(c1>=1):
        print(1)
    if(c2>=1):
        print(2)
    if(c3>=1):
        print(3)
