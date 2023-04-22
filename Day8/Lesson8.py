# ფუნქციური პროგრამირება - functional programming
def happy_day(name,day):
       print(name + " " + "bednieri dge" + " " +  str(day) + " " + "noemberi")
happy_day("anas",15)
 
# N2
students=["ana", "tushy", "taia"]
new_arr=[]
i=len("hym")
while i > 0:
    new_arr.append(students[i-1])
    i -= 1
print(new_arr) 

# შევკრიბოთ მნიშვნელობები
def shekreba(num1,num2,num3,num4):
      print(num1+num2+num3+num4)
shekreba(20,24.1,25.7,3)

# მაქსიმალური რიცხვის გამოსახვა while- მეთოდით
score=[12,25,33,45,67,5,64]
max_num=score[0]
i=0
while i < len(score):
      if score[i] > max_num : 
            max_num=score[i]
      i += 1
print(max_num)

        
