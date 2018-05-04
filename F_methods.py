from os import remove, rename


def Write(file_name):

    try:
        with open(file_name + '.txt', 'a') as write:
            while True:
                ID, name, age = input('Enter Your ID: '), input('Enter Your Name: '), input('Enter Your Age: ')
                print(ID + '\t' + name + '\t' + age, file=write)
                Q = input('Continue[Y/N]??: ')
                if Q == 'N' or Q == 'n':
                    break

    except Exception as exp:
        print('File Error ' + str(exp))


def Read(file_name):

    try:
        with open(file_name+'.txt') as read_file:
            for each_line in read_file:
                print(each_line, end='')

    except Exception as exp:
        print('File Error ' + str(exp))


def Update(file_name):

    try:
        found = False
        with open(file_name + '.txt') as update_file, open('temp.txt', 'w') as temp:
            ID = input("Enter ID to update it's Record: ")
            for each_line in update_file:
                update_list = each_line.split()
                if update_list[0] == ID:
                    update_list[0], update_list[1], update_list[2] = input('Enter new ID: '), input('Enter new Name: '), input('Enter new Age: ')
                    temp.write('{0}\t{1}\t{2}\n'.format(update_list[0], update_list[1], update_list[2]))
                    found = True
                else:
                    temp.write(each_line)

            if not found:
                print('Record Not Found')

            remove(file_name + '.txt')
            rename('temp.txt', file_name + '.txt')

    except Exception as exp:
        print('File Error '+ str(exp))

def Delete(file_name):

    try:
        found = False
        Id = input("Enter ID to Delete it's Record: ")
        with open(file_name + '.txt') as delete_file, open('temp.txt', 'w') as temp:
            for each_line in delete_file:
                delete_list = each_line.split()
                if delete_list[0] != Id:
                    temp.write('%s' % each_line)
                if delete_list[0] == Id:
                    found = True

            if not found:
                print('Record not found')
            remove(file_name+'.txt')
            rename('temp.txt', file_name+'.txt')

    except Exception as exp:
        print('File Error: '+ str(exp))

def Search(file):

    try:
        found = False
        ID = input("Enter ID to Find It's Record: ")
        with open(file + '.txt') as search_file:
            for each_line in search_file:
                s = each_line.split()
                if s[0] == ID:
                    print(each_line, end='')
                    found = True
                    break

            if not found:
                print('Record Not Found')

    except Exception as exp:
        print('File Error ' + str(exp))
