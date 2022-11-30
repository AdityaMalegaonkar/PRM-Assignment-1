def checktriangle(tside1, tside2, tside3):
     
    if (tside1 + tside2 <= tside3) or (tside1 + tside3 <= tside2) or (tside2 + tside3 <= tside1) :
        return False
    else:
        return True       
 
print("\nTriangle Validation\n")
tside1 = int(input("Enter length of first side : "))
tside2 = int(input("Enter length of second side : "))
tside3 = int(input("Enter length of third player : "))

def checkrectangle(rside1 , rside2 , rside3 , rside4):
    
    if rside1 == rside3 and rside2 == rside4:
        return True
    else:
        return False

print("\nRectangle Validation\n")
rside1 = int(input("Enter length of first side : "))
rside2 = int(input("Enter length of second side : "))
rside3 = int(input("Enter length of third side : "))
rside4 = int(input("Enter length of fourth side : "))

if checktriangle(tside1, tside2, tside3):
    print("Valid Triangle")
else:
    print("Invalid Triangle")
if checkrectangle(rside1 , rside2 , rside3 , rside4):
    print("Valid rectangle")
else:
    print("Invalid rectangle")