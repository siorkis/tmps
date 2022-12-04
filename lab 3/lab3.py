"""Here we attempt to make an organizational hierarchy with sub-organization,
which may have subsequent sub-organizations, such as:
Software-engineering				[Composite]
    FAF-202								 [Composite]
            Student1.1					 [Leaf]
            Student2.1					 [Leaf]
    FAF-203								 [Composite]
            Student1.2					 [Leaf]
            Student2.2					 [Leaf]

Composite patter """


class LeafElement:
    """Class representing objects at the bottom or Leaf of the hierarchy tree."""

    def __init__(self, *args):
        """'Takes the first positional argument and assigns to member variable "position"."""
        self.position = args[0]

    def showDetails(self):
        """Prints the position of the child element."""
        print("\t", end="")
        print(self.position)


class CompositeElement:
    """Class representing objects at any level of the hierarchy
    tree except for the bottom or leaf level. Maintains the child
    objects by adding and removing them from the tree structure."""

    def __init__(self, *args):
        """Takes the first positional argument and assigns to member
        variable "position". Initializes a list of children elements."""
        self.position = args[0]
        self.children = []

    def add(self, child):
        """Adds the supplied child element to the list of children
        elements "children"."""
        self.children.append(child)

    def remove(self, child):
        """Removes the supplied child element from the list of
        children elements "children"."""
        self.children.remove(child)

    def showDetails(self):
        """Prints the details of the component element first. Then,
        iterates over each of its children, prints their details by
        calling their showDetails() method."""
        print(self.position)
        for child in self.children:
            print("\t", end="")
            child.showDetails()


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class WrittenText:
    """Represents a Written text """

    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


# decorator pattern
class UnderlineWrapper(WrittenText):

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        msg = "{}".format(self._wrapped.render())
        return color.UNDERLINE + msg + color.END


class BoldWrapper(WrittenText):

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        msg = "{}".format(self._wrapped.render())
        return color.BOLD + msg + color.END


"""Bridge Method. We have a Student class having three attributes
named as math, physics, and computer_science and two
methods named as produceWithAPIOne(), produceWithAPITwo().
Our purpose is to separate out implementation
specific abstraction from implementation-independent
abstraction"""


class ProducingAPI1:
    """Implementation specific Abstraction"""

    def produce_student(self, math, physics, computer_science):
        print(f'API1 is producing student with notes: Math = {math}, '
              f'Physics = {physics} and Computer_science = {computer_science}')


class ProducingAPI2:
    """Implementation specific Abstraction"""

    def produce_student(self, math, physics, computer_science):
        print(f'API2 is producing student with notes: Math = {math}, '
              f'Physics = {physics} and Computer_science = {computer_science}')


class Student:

    def __init__(self, math, physics, computer_science, producingAPI):
        """Initialize the necessary attributes Implementation independent Abstraction"""

        self._math = math
        self._physics = physics
        self._computer_science = computer_science

        self._producingAPI = producingAPI

    def produce(self):
        """Implementation specific Abstraction"""

        self._producingAPI.produce_student(self._math, self._physics, self._computer_science)


class Create:
    # Subsystem 1

    @staticmethod
    def create():
        print("creating...")


class Read:
    # Subsystem 2

    @staticmethod
    def read():
        print("Reading...")


class Update:
    # Subsystem 3

    @staticmethod
    def update():
        print("Updating...")


class Delete:
    # Subsystem 4

    @staticmethod
    def delete():
        print("Deleting...")


# Facade pattern
class Crud:
    """Facade"""

    def __init__(self):
        self.creating = Create()
        self.reading = Read()
        self.updating = Update()
        self.deleting = Delete()

    def perform_crud(self):
        self.creating.create()
        self.reading.read()
        self.updating.update()
        self.deleting.delete()


class College:

    def studyingInCollege(self):
        answer = WrittenText("Studying In College....")
        print(BoldWrapper(answer).render())


# proxy pattern - we reduce load on the abstract DB by proxy class
# [client] -> [proxy] -> [server]
class CollegeProxy:

    def __init__(self):
        self.feeBalance = 1000
        self.college = None

    def studyingInCollege(self):

        print("Proxy in action. Checking to see if the balance of student is clear or not...")
        if self.feeBalance <= 500:
            # If the balance is less than 500, let him study.
            self.college = College()
            self.college.studyingInCollege()
        else:
            # Otherwise, don't instantiate the college object.
            answer = WrittenText("Your fee balance is greater than 500, first pay the fee")
            print(UnderlineWrapper(answer).render())


if __name__ == "__main__":

    collegeProxy = CollegeProxy()

    # Client attempting to study in the college at the default balance of 1000.
    # Logically, since he / she cannot study with such balance,
    # there is no need to make the college object.
    collegeProxy.studyingInCollege()

    # Altering the balance of the student
    collegeProxy.feeBalance = 100

    # Client attempting to study in college at the balance of 100. Should succeed.
    collegeProxy.studyingInCollege()

    topLevelMenu = CompositeElement("Software-engineering")
    subMenuItem1 = CompositeElement("FAF-202")
    subMenuItem2 = CompositeElement("FAF-203")
    subMenuItem11 = LeafElement("Student1.1")
    subMenuItem12 = LeafElement("Student1.2")
    subMenuItem21 = LeafElement("Student2.1")
    subMenuItem22 = LeafElement("Student2.2")
    subMenuItem1.add(subMenuItem11)
    subMenuItem1.add(subMenuItem12)
    subMenuItem2.add(subMenuItem22)
    subMenuItem2.add(subMenuItem22)

    topLevelMenu.add(subMenuItem1)
    topLevelMenu.add(subMenuItem2)
    topLevelMenu.showDetails()

    student1 = Student(9, 8, 10, ProducingAPI1())
    student1.produce()

    student2 = Student(7, 9, 6, ProducingAPI2())
    student2.produce()

    student3 = Student(5, 6, 5, ProducingAPI1())
    student3.produce()

    student4 = Student(10, 10, 10, ProducingAPI2())
    student4.produce()

    new_student_record = Crud()
    new_student_record.perform_crud()
