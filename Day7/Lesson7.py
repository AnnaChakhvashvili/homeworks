# დავალაგოთ რიცხვები ზრდადობის  მიხედვით 
scores=[18,24,8,9,22,20,84]
scores.sort()
print(scores)

# გავიგოთ ამ რიცხვების მაქსიმალური და მინიმალური მნიშვნელობა
scores=[1,4,8,9,22,20,64]
print(scores[-1])
print(scores[0])

# სტუდენტთა სია ანბანის მიხედვით
students=["mari","gio","beqa","ana"]
students.sort()
print(students)

# შევაბრუნოთ
students=["mari","gio","beqa","ana"]
students.sort(reverse=True)
print(students)

# წაიშალოს ელემენტები სადაც მეორე ასო არის - a
menu=["lavashi","tevzi","xili"]
for food in menu:
    if food[1] == "a":
        menu.remove(food)
print(menu)

# სიტყვის ჩამატება
list=["a","b","c","e"]
list.insert(3,"d")
print(list)