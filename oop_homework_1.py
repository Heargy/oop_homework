class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lector, course, grade):
        if (isinstance(lector, Lectors) and course in self.courses_in_progress or
                course in self.finished_courses and course in lector.courses_attached):
            if 0 < grade < 10:
                if course in lector.grades:
                    lector.grades[course] += [grade]
                else:
                    lector.grades[course] = [grade]
            else:
                return 'Error'
        else:
            return 'Error'

    def average_rate_of_hw(self):
        return sum(map(sum, self.grades.values()))/sum(map(len, self.grades.values()))

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_rate_of_hw():.2f}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}\n')

    def __eq__(self, other):
        return self.average_rate_of_hw() == other.average_rate_of_hw()

    def __lt__(self, other):
        return self.average_rate_of_hw() < other.average_rate_of_hw()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lectors(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rate_of_lecture(self):
        return sum(map(sum, self.grades.values()))/sum(map(len, self.grades.values()))

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_rate_of_lecture():.2f}\n')

    def __eq__(self, other):
        return self.average_rate_of_lecture() == other.average_rate_of_lecture()

    def __lt__(self, other):
        return self.average_rate_of_lecture() < other.average_rate_of_lecture()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if 0 < grade < 10:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Error'
        else:
            return 'Error'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.finished_courses += ['Введение в программирование']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Java']

cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Java', 7)
cool_mentor.rate_hw(best_student, 'Python', 9)

cool_lector = Lectors('Some', 'Buddy')
cool_lector.courses_attached += ['Python']
cool_lector.courses_attached += ['Java']

best_student.rate_lecture(cool_lector, 'Java', 8)
best_student.rate_lecture(cool_lector, 'Java', 8)
best_student.rate_lecture(cool_lector, 'Python', 9)

fool_student = Student('Ruoy', 'Eman', 'your_gender')
fool_student.courses_in_progress += ['Python']
fool_student.courses_in_progress += ['Java']
fool_student.finished_courses += ['Введение в программирование']

cool_mentor.rate_hw(fool_student, 'Python', 2)
cool_mentor.rate_hw(fool_student, 'Java', 3)
cool_mentor.rate_hw(fool_student, 'Python', 4)

print(cool_lector)

print(best_student == fool_student)
