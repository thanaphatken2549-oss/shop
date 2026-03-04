print(" *** Number Fun !!! ***")
a,b = input("Enter a b : ").split()
print("a=",a,"\ttype =",type(a))
print("b=",b,"\ttype =",type(b))
print("a+b =>",a,"+",b,"=>",a+b)
# convert a to int
# convert b to int
# แสดงผล a/b ทศนิยม 2 ตำแหน่ง
# แสดงผล b/a ทศนิยม 3 ตำแหน่ง
# แสดงผลการหารแบบเหลือเศษของ a และ b
# แสดงผลการหารแบบเหลือเศษของ b และ a
a = int(a)
b = int(b)
print("a/b =",f"{a/b:.2f}")
print("b/a =",f"{b/a:.3f}")
print("a/b =",a//b,"r",a%b)
print("b/a =",b//a,"r",b%a)