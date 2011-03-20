
class CourseSearchParams:
    def __init__(self, department=None, number=None, section=None, instructor=None):
        self.department = department;
        self.number = number;
        self.section = section;
        self.instructor = instructor;