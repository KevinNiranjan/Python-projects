# Project:Find even and odd numbers from a list, and store them separately in a new list


scrambled = [23, 25, 26, 22, 78, 76, 75, 73, 23, 11, 26, 70, 34, 67, 69, 80]
even = []
odd = []
for i in scrambled:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("even list=",even)
print("odd list=",odd)
