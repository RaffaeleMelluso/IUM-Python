array = list(range(0,10))
print("Esercizio 1",array[8:3:-1])
def moltiplica(x,y):
    x,y= 2*x, 2*y
    return [x, y]
print(f"Esercizio 2: 3, 5, {moltiplica(3,5)}")
dict = {
    "name" : "Marco",
    "surname" : "Rossi",
    "dob" : "01/01/1990",
    "age" : 30
}
print("Esercizio 3", dict)
del dict["name"]
print("Esercizio 4", dict)
lista = [1, 2, 3, 4, 0, 1, 2, 0, 3]
print("Esercizio 5", [x for x in lista if x])

l1, l2= [1, 2, 3, 4],[0, 1, 2, 0, 3]
print("Esercizio 6", sorted(l2+l1))

dict_list = [
    {
        "name" : "Marco",
        "surname" : "Rossi",
        "sex": "male",
        "dob" : "01/01/1990",
        "age" : 30
    },
    {
        "name": "Anna",
        "surname": "Bianchi",
        "sex": "female",
        "dob": "01/01/1990",
        "age": 10
    }
]
sorted_list= sorted(dict_list, key=lambda x: x["name"])
print("Esercizio 7", sorted_list)
print("Esercizio 7", [x for x in dict_list if x["sex"]=="female"])
set1 = {"red", "white", "green"}
set1.add("black")
set1.remove("red")
print("Esercizio 8", set1, "\nC'è il bianco?" ,"white" in set1)
