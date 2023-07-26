if __name__ == '__main__':
    records = []
    for _ in range(int(input("Rango: "))):
        name = input("Name: ")
        score = float(input("Score: "))
        records.append([name,score])
    
    min_note = 100
    min_note_2 = 100

    for student in records:
        if student[1]<=min_note:
            min_note = student[1]

    for student in records:
        if (student[1]<=min_note_2) and (student[1]>min_note):
            min_note_2 = student[1]
        elif (records[-1][1] == min_note):
            min_note_2 = min_note

    students = []
    
    for student in records:
        if student[1]==min_note_2:
            students.append(student[0])

    students.sort()
    for name in students:
        print(name)
    
        
    