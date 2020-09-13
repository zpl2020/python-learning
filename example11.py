class User():
    def __init__(self, name, type):
        self.login_attempts = 0
        self.name = name
        self.type = type

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(str(self.name) + ' has tried for ' + str(self.login_attempts) + ' times.')
        if self.type == 's':
            print('Sorry, but the computer is locked.')
        elif self.type == 't':
            print('You have 2 chances to go.')
        elif self.type == 'a':
            print('Administrators do not need to enter passcodes.')
        else:
            print('Enter again.')

    def reset_login_attempts(self):
        self.login_attempts = 0
        print('Reset login attempts.')

A = input('Student Name: ')
C = input('Student or teacher: ')
inst1 = User(A, C)
inst1.increment_login_attempts()
inst1.increment_login_attempts()
inst1.increment_login_attempts()
inst1.increment_login_attempts()
inst1.reset_login_attempts()


class Teachers(User):
    def __init__(self, t_name, subject):
        super().__init__(t_name, type)
        self.subject = subject

    def print_subjects(self):
        print(str(self.name) + ' is teaching ' + str(self.subject) + '.')

    def check_login_attempts(self):
        self.login_attempts += 1

A = input('Teacher name: ')
B = input('Subject name: ')
inst1 = Teachers(A, B)
inst1.print_subjects()
inst1.increment_login_attempts()
inst1.increment_login_attempts()
inst1.increment_login_attempts()
inst1.increment_login_attempts()
inst1.reset_login_attempts()


class Admin(User):
    def __init__(self, name, type, privileges):
        self.name = name
        self.type = type
        self.privileges = privileges
        super().__init__(privileges, type)