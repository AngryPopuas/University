First = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4] 
Second = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4] 
Third = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

MassiveCopy = []
for i in range(len(First)):
    if First[i] == 3:
        MassiveCopy.append(4)
        continue
    if First[i] == 2:
        continue
    MassiveCopy.append(First[i])
print(MassiveCopy)

MassiveCopy = []
for i in range(len(Second)):
    if Second[i] == 3:
        MassiveCopy.append(4)
        continue
    if Second[i] == 2:
        continue
    MassiveCopy.append(Second[i])
print(MassiveCopy)

MassiveCopy = []
for i in range(len(Third)):
    if Third[i] == 3:
        MassiveCopy.append(4)
        continue
    if Third[i] == 2:
        continue
    MassiveCopy.append(Third[i])
print(MassiveCopy)
