subjects = ["Maths  ","Science","Social "]
Quarterly = []
Halfyearly = []
Annual =[]
count = MTotal = 0

studentid = input("Enter your Student Id ")

for x in subjects:
    a = int(input("Enter Quarterly marks for " + x))
    b = int(input("Enter Halfyearly marks for " + x))
    c = int(input("Enter Annual marks for " + x))
    Quarterly.append(a)
    Halfyearly.append(b)
    Annual.append(c)

print("\n\t\t SUBJECTS             QUARTERLY     HALFYEARLY       ANNUAL      TOTAL")
for (x, y, z, a) in zip(subjects, Quarterly, Halfyearly, Annual):
    print("\n\t\t", x, "           ", y, "           ", z, "           ", a, "           ", y + z + a)
    MTotal = MTotal + y + z + a
    if y + z + a < 100:
        count = count + 1

    if count == 0:
        print("\n\t\tTOTAL MARKS: ", MTotal, "\t\tRESULT: PASS")
    else:
        print("\n\t\tTOTAL MARKS:", MTotal, "\t\tRESULT: FAIL")