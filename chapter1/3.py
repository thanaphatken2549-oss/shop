try : 
    a,b,c,d = map(int,(input("Enter your input : ").split()))
except :
    print("Invalid Input")
    exit()
be = (a*60)+b
af = (c*60)+d
time = af-be
mtime = round(time)
if b > 59:
    print("Invalid Input")
elif d > 59:
    print("Invalid Input")
elif a < 7:
    print("Invalid Input")
elif a == 23 and b >= 1:
    
    print("Invalid Input")
elif c == 23:
    d >= 1
    print("Invalid Input")
elif af-be < 0:
    print("Invalid Input")
elif a == 0:
    print("Invalid Input")
elif 0 < time <= 15:
    print(0)
elif 15 < time <= 60:
    print(10)
elif 60 < time <= 120:
    print(20)
elif 120 < time <= 180:
    print(30)
elif 180 < time <= 240:
    print(50)
elif 240 < time <= 300:
    print(70)
elif 300 < time <= 360:
    print(90)
elif 360 < time <= 960:
    print(200)
elif af-be < 0:
    print("Invalid Input")