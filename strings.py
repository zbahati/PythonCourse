course = 'Python for Beginners'
another = course[:]
print(another)

print(another[1:-1])
print(another[:5])
print(another[5:])


# sting format

print(f'{course} is the best course with only {len(another)} characters long')

print(course.upper())
print(course.lower())

print(course.find('Python'))
print(course.replace('Python', 'Django'))

print('Python' in course)
