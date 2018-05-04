
import F_methods as File
import os

os.system('clear')

file_Name = input('Enter file name: ')
file_Name = file_Name.split('.', 1)


while True:
    
    ch = int(input('\n1)Add Records\n2)Read All Records\n3)Delete Record\n4)Update Record\n5)Find Record\n0)Exit\n>>> '))
    if ch == 1:
        File.Write(file_Name[0])
    elif ch == 2:
        File.Read(file_Name[0])
    elif ch == 3:
        File.Delete(file_Name[0])
    elif ch == 4:
        File.Update(file_Name[0])
    elif ch == 5:
        File.Search(file_Name[0])
    else:
        exit(0)


