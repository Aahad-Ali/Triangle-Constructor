from triangle import Triangle

#default constructor object
t1 =Triangle()
print(t1)

#Equilateral  constructor object
t2=Triangle(3)
print(t2)

#Isosceles  constructor object
t3=Triangle(3,5)
print(t3)

#Scalene constructor object
t4=Triangle(3,5,9)
print(t4)

#clone constructor object
t5=Triangle(t2)
print(t5)


#Perimeter Calculate
print(f"perimeter of t3:{t3.perimeter()}")

#Right-Angled Triangle Check
print(f"Is t3 a right-angled triangle? {t3.is_right_angled()}")


# Getter aur Setter Test
print(f"Original SideA of t2: {t2.sideA}")
t2.sideA = 10
print(f"Updated SideA of t2: {t2.sideA}")

# Total triangle count
print(f"Total Triangle Objects Created: {Triangle.object_count}")
