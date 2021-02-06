def menu():   
    print("*****************************************")
    print("********* Gestió d'alumnes **************")
    print("*****************************************")
    print("1. Introdueix alumnes")
    print("2. Mostra els alumnes")
    print("3. Analitza els registres")
    print("4. Sortir del programa")
    case = int(input("Seleccione una opció: "))
    if case == 1:
       repeat()

    if case == 2:
        show()
            
    if case == 3:
        analytics()

    if case == 4:
        close()
def repeat():
    import csv
    import os
    number = int(input("Indica el nombre d'alumnes que vols introduir: "))
    for i in range(number):
        student_ID = int(input("Introdueix l'identificador: "))
        first_name = input("Introdueix el nom de l'estudiant: ")
        last_name = input("Introdueix el cognom de l'estudiant: ")
        subject = input("Introdueix l'assignatura: ")
        grade = int(input("Introdueix la nota: "))

        student = {
        "student_ID": student_ID,
        "first_name": first_name,
        "last_name": last_name,
        "subject": subject,
        "grade": grade
        }

        if os.path.isfile('students.csv'):
            with open('students.csv', 'a', encoding='utf-8', newline='') as csvfile:
                fieldnames = ['student_ID', 'first_name', 'last_name', 'subject','grade']
                writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writeCSV.writerow({'student_ID': student_ID, 'first_name': first_name,'last_name': last_name, 'subject': subject, 'grade': grade})
        else:
                fieldnames = ['student_ID', 'first_name', 'last_name', 'subject','grade']
                with open('students.csv', 'w', encoding='utf-8', newline='') as csvfile:
                    writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writeCSV.writeheader()
                    writeCSV.writerow({'student_ID': student_ID, 'first_name': first_name,'last_name': last_name, 'subject': subject, 'grade': grade})
    end()
def show():
    import os
    import csv
    if os.path.isfile('students.csv'):
        with open('students.csv', encoding="utf8") as csvfile:
            readCSV = csv.DictReader(csvfile, delimiter=',')
            for row in readCSV:
                print(f"Estudiant {row['student_ID']}: {row['first_name']}{row['last_name']}, a la matèria {row['subject']} ha obtingut un{row['grade']}.")

    else:
        print("Encara no hi ha cap fitxer. Crea un amb la opció 1")
        menu()
    end()
def analytics():
    import os
    import csv
    import pandas as pd
    if os.path.isfile('students.csv'):
        print("¿Quants registres vols consultar?")
        print("1. Tots")
        print("2. Els n primer registres")
        print("3. Els n ultims registres")
        case = int(input("Selecciona una opció: "))
        if case == 1:
            with open('students.csv', encoding="utf8") as csvfile:
                readCSV = csv.DictReader(csvfile, delimiter=',')
                for row in readCSV:
                    print(f"Estudiant {row['student_ID']}: {row['first_name']}{row['last_name']}, a la matèria {row['subject']} ha obtingut un{row['grade']}.")
        if case == 2:
            df = pd.read_csv('students.csv')
            print("¿Quantes lineas vols consultar?")
            options = int(input("Número de lineas: "))
            print(df.dtypes)
            print(df.head(options))

        if case == 3:
            df = pd.read_csv('students.csv')
            print("¿Quantes lineas vols consultar?")
            options = int(input("Número de lineas: "))
            print(df.dtypes)
            print(df.tail(options))
    else:
        print("Encara no hi ha cap fitxer. Crea un amb la opció 1")
        menu()
    end()
def end():
    print("¿Que vols fer ara?")
    print("1. Tornar al menu principal")
    print("2. Analitzar registres")
    print("3. Sortir del programa")
    case = int(input("Seleccione una opció: "))
    if case == 1:
        menu()

    if case == 2:
        analytics()
            
    if case == 3:
        close()

def close():
    print("Adeu!")
