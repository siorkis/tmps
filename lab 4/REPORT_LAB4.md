# TMPS lab 4


## TOPIC: Behavioral Design Patterns

## ## Objectives:
&ensp; &ensp; __1. Study and understand the Behavioral Design Patterns.__

&ensp; &ensp; __2. As a continuation of the previous laboratory work, think about what communication between software entities might be involed in your system.__

&ensp; &ensp; __3. Implement some additional functionalities using behavioral design patterns.__


## Main tasks :
&ensp; &ensp; __1. By extending your project, implement at least 1 behavioral design pattern in your project:__
  * The implemented design pattern should help to perform the tasks involved in your system.
  * The behavioral DPs can be integrated into you functionalities alongside the structural ones.
  * There should only be one client for the whole system.
  
## IMPLEMENTATION

Imagine you are going to take admission in one of the elite courses offered by Coursera such as DSA, IOS, and BD. 
Initially, there are very few students who are approaching to join these courses. Initially, the developer can create separate objects and classes for the connection between the students and the courses but as the courses become famous among students it becomes hard for developers to handle such a huge number of sub-classes and their objects.
We can create a separate mediator class named as Course and a User Class using which we can create different objects of Course class. In the main method, we will create a separate object for each student and inside the User class, we will create the object for Course class which helps in preventing the unordered code.


```python 
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

```
