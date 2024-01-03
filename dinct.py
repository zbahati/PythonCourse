students = [
  {
    'name': "Bahati",
    'age': 25,
    'address': 'Gisenyi'
  },
  {
    'name': "Bahati3",
    'age': 25,
    'address': 'Muhanga'
  },
  {
    'name': "bahati2",
    'age': 25,
    'address': 'Kigali'
  },
  {
    'name': "bahati1",
    'age': 24,
    'address': 'Rubavu'
  }
]

for student in students:
  print(student["name"][0:3],student['age'], student['address'],sep='-')