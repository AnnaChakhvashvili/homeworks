# X - საიტერაციო ცვლადი 
for X in range(0,6):
    print("Ana")
    X += 1     
#   X += 1   თუ ამ ცვლადს დავაკომენტარებთ მივიღებთ "Ana"- ს უსასრულოდ

# ჩავწერთ სხვაობით 
for X in range(8-4):
    print("Tushy")
    X += 1    

# range(4,12,3) - 4 დან 12 ჩათვლით ოველი მესამე 
for X in range(4,12,3):
    print("Ana")
    X += 1     

# სანამ ნაკლებია 15-ზე  იპრინტება "ATAY"
X=0
while  X < 15:
    print("ATAY")
    X += 1
# N-1
full_name = "Ana Chakhvashvili"
X = 0
while  X < len(full_name):
    print(full_name[X])
    X += 12
#  N-2
full_name = "Ana"
X = 0
while  X < len(full_name):
    print(2)
    X += 1

# შემოვიტანოთ a და  b , ტერმინალში დაპრინტვის შედეგად უნდა მივიღოთ AG, BK, DL.
a="ABCD"
b="GKL"
x=0
while x < len(a) > len(b):
    print("A" + "G")
    print("B" + "K")
    print("D" + "L")
    x += 4
# and - კავშირში ერთ-ერთი თუ არასწორია უკვე მცდარია , მხოლოდ ორივეს ჭეშმარიტების შემთხვევაშია True.
if 14 > 9 and 17<30:
    print("cool")

# A
if (1==1) and (2+7>4):
    print("+")
else:
    print("-")
