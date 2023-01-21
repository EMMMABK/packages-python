class staff: 
    def __init__(self, deleted, now): 
        self.deleted = deleted 
        self.now = now 
        self.deleted__list__of__staff = ['Carl Johnson', 'Harry Clark', 'Nurlan'] 
        self.now__list__of__staff = ['Kairat Dos, Daniar Chik']
    def deleted(self, name, surname):
        print('What you want to delete or add?')
        choice__to__deleted = int(input('If you want to delete the smbd - 1, if you want to add -2'))
        if choice__to__deleted == 1:
            self.deleted__list__of__staff.append(name, surname)
        elif choice__to__deleted == 2:
            self.deleted__list__of__staff.remove(name, surname)
        else:
            print("I didn't understand you!")
    def now(self,name, surname):
        print('What you want to delete or add?')
        choice__to___now = int(input('If you want to delete the smbd - 1, if you want to add -2'))
        if choice__to___now == 1:
            self.now__list__of__staff.append(name, surname)
        elif choice__to___now == 2:
            self.now__list__of__staff.remove(name, surname)
        else:
            print("I didn't understand")
class group:
    def __init__(self, deleted, now):
        self.deleted = deleted
        self.now = now
        students__in__group = Student()
        self.deleted__list__of__groups = [].append(Student) 
        # К каждому списку листов привязать список студентов
        self.now__list__of__groups = [].append(Student)
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        list__of__students = []
    def add(self, name,surname):
        self.list__of__students.append(name, surname)
class admin: 
    def __init__(self, staff, group): 
        self.staff = staff 
        self.group = group 
    def staff(self): 
        print('Staff:', staff) 
        print('Group:', group)

