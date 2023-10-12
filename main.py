f = open('students_new.txt', 'r', encoding='utf-8')

students = []
for student in f:
    line = student.split(';')
    students.append({'id':int(line[0]), 'name':line[1], 
                     'var':int(line[2]), 'subgroup':int(line[3])})

surname = input('enter surnmae: ')
for i in students:
    name = str(i['name'])
    endSurname = name.find(' ')
    if name[0:endSurname].lower() == surname.lower():
        print(f"id - {i['id']}\nname - {i['name']}\nvar - {i['var']}\nsubgroup - {i['subgroup']}")
        break

f.close()