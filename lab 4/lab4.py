class Course(object):
    """Mediator class."""

    def displayCourse(self, user, course_name):
        print("[{}'s course ]: {}".format(user, course_name))


class User(object):
    """A class whose instances want to interact with each other."""

    def __init__(self, name):
        self.name = name
        self.course = Course()

    def sendCourse(self, course_name):
        self.course.displayCourse(self, course_name)

    def __str__(self):
        return self.name

if __name__ == "__main__":
    Andrew = User('Andrew')  # user object
    Mike = User('Mike')  # user object
    Lisa = User('Lisa')  # user object

    Andrew.sendCourse("Data Structures and Algorithms")
    Mike.sendCourse("IOS development")
    Lisa.sendCourse("Big Data")
