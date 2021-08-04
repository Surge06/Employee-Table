emp = { 'ID':[],
        'Name':[],
        'Dept':[],
        'Desg':[],
        'Join':[],
        'Status':[]
        }
idx = 0
inpt = ''
print('Emplployee menu')
print('1: Add entry')
print('2: Delete entry')
print('3: Search for a particular entry')
print('4: Update an entry')

w = open('example.csv', 'w')
w.write('Employee ID, Employee Name, Department, Designation, Join Date, Employee Status \n')
w.close()

def new(emp):
    ID = input('Enter ID: ')
    if ID in emp['ID']:
        print('Duplicate ID')
    else:
        name = input('Enter name: ')
        dept = input('Enter department: ')
        desg = input('Enter designation: ')
        join = input('Enter join date: ')
        status = input('Enter employment status: ')
        emp['ID'].append(ID)
        emp['Name'].append(name)
        emp['Dept'].append(dept)
        emp['Desg'].append(desg)
        emp['Join'].append(join)
        emp['Status'].append(status)
        with open('example.csv','a') as apnd:
            apnd.write('{}, {}, {}, {}, {}, {} \n'.format(ID, name, dept, desg, join, status))
        apnd.close()
        
def rmv(emp):
        idx = 0
        sel = int(input('Choose ID: '))
        for i in emp['ID']:
            while idx != sel:
                idx += 1
        idx -= 1
        print('ID:', emp['ID'][idx], 'Name:',emp['Name'][idx], 'Department:', emp['Dept'][idx], emp['Desg'][idx], emp['Join'][idx], emp['Status'][idx])
        
        dlt = input('Delete this record? ')
        if dlt in ['Y', 'yes', 'y', 'YES']:
            del emp['ID'][-1]
            del emp['Name'][idx]
            del emp['Dept'][idx]
            del emp['Desg'][idx]
            del emp['Join'][idx]
            del emp['Status'][idx]
            
            with open('example.csv', 'w') as d:
                d.write('Employee ID, Employee Name, Department, Designation, Join Date, Employee Status \n')
            d.close()
            with open('example.csv', 'a') as apnd:
                for i in range(0, len(emp['ID'])):
                    apnd.write('{}, {}, {}, {}, {}, {} \n'.format(emp['ID'][i],emp['Name'][i],emp['Dept'][i], emp['Desg'][i], emp['Join'][i],emp['Status'][i]))
            apnd.close()


def prt(emp):
    print('|{0:<15}|{1:<20}|{2:<15}|{3:<15}|{4:<15}|{5:<16}|'.format('Employee ID','Employee name','Department','Designation', 'Join Date','Employee status'))
    print('-' * 103)
    for i in range(0, len(emp['ID'])):
        print('|{0:<15}|{1:<20}|{2:<15}|{3:<15}|{4:<15}|{5:<16}|'.format(emp['ID'][i],emp['Name'][i],emp['Dept'][i], emp['Desg'][i], emp['Join'][i],emp['Status'][i]))
    print('-' * 103, '\n')
    

def upd(emp, column, entry):
    search = input('Enter an employee %s: ' % entry)
    print('No entries found') if search not in emp[column] else print('Entires found:')
    for i in range(0, len(emp[column])):
        if search in emp[column][i]:
            print('ID:', emp['ID'][i], 'Name:', emp['Name'][i], 'Department:',emp['Dept'][i], 'Designation:', emp['Desg'][i], 'Join Date:', emp['Join'][i], 'Status:', emp['Status'][i])
        else:
            continue
def srch_choice():
    column = input('Choose a column to search from: ')
    entry = ''
    if column in ['ID' , 'id', 'Id']:
        column = 'ID'
        entry = 'ID' 
        srch(emp, column, entry)
    elif column in ['Name', 'name', 'Name', 'NAME']:
        column = 'Name'
        entry = 'name' 
        srch(emp, column, entry)
    elif column in ['Dept', 'dept', 'DEPT', 'department', 'Department']:
        column = 'Dept'
        entry = 'department' 
        srch(emp, column, entry)
    elif column in ['desg', 'DESG','Desg', 'Designation', 'designation']:
        column = 'Desg'
        entry = 'designation' 
        srch(emp, column, entry)
    elif column in ['join', 'JOIN',  'Join Date', 'Join', 'Join date', 'join date']:
        column = 'Join'
        entry = 'join date' 
        srch(emp, column, entry)
    elif column in ['Status', 'status', 'STATUS']:
        column = 'Status'
        entry = 'status' 
        srch(emp, column, entry)
    else:
        print('Invalid column name')
        
def srch(emp, column, entry):
    search = input('Enter an employee %s: ' % entry)
    print('No entries found') if search not in emp[column] else print('Entires found:')
    for i in range(0, len(emp[column])):
        if search in emp[column][i]:
            print('ID:', emp['ID'][i], 'Name:', emp['Name'][i], 'Department:',emp['Dept'][i], 'Designation:', emp['Desg'][i], 'Join Date:', emp['Join'][i], 'Status:', emp['Status'][i])
        else:
            continue
                
while inpt != 'quit':
    inpt = input('Input: ')
    if inpt == '1':
        new(emp)
    elif inpt == '2':
        rmv(emp)
    elif inpt == '3':
        srch_choice()
    elif inpt == '4':
        prt(emp)
    else:
        continue

