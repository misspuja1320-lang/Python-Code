m=int(input("Enter the marks:"))
mark=m//10
match(mark):
   case 10|9:
       print("grade=O")
   case 8:
       print("grade=E")
   case 7:
       print("grade=A")
   case 6:
       print("grade=B")
   case 5:
       print("grade=C")
   case 4:
       print("grade=E")
   case _:
       print("fail")