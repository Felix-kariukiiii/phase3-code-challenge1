def sort_by_age(people):
    
    return sorted(people, key=lambda x: x[1])

people = [("Alice", 25), ("Bob", 30), ("Charlie", 20), ("David", 35)]
sorted_people = sort_by_age(people)
print(sorted_people)  

