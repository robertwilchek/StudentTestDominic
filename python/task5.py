with open('students.csv', 'r') as file:
    data = file.read()

records = data.split()

listed_records = []
for record in records[1:]:
    listed_records.append(record.split(','))

listed_records.sort(key = lambda x: x[1], reverse=True)

print(records[0])

for record in listed_records:
    print((',').join(record))

with open('students_reversed.csv', 'w') as file:
    file.write(records[0])
    file.write('\n')

    for record in listed_records:
        file.write((',').join(record))
        file.write('\n')