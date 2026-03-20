"""
NB: Some exercises have multiple parts, and you can receive points for the different parts separately. You can submit a partially completed exercise by choosing 'Submit Solution' from the menu next to the button for executing tests .

In this exercise you will write two different classes, which will in turn form the backbone of the programming exercise which follows this one, where you will write an interactive application.

Task

Please write a class named Task which models a single task in a software company's list of tasks. Tasks have

a description
an estimate of the hours required for completing the task
the name of the programmer assigned to the task
a field for keeping track of whether the task is finished
a unique identifier
The class is used as follows:

t1 = Task("program hello world", "Eric", 3)
print(t1.id, t1.description, t1.programmer, t1.workload)
print(t1)
print(t1.is_finished())
t1.mark_finished()
print(t1)
print(t1.is_finished())
t2 = Task("program webstore", "Adele", 10)
t3 = Task("program mobile app for workload accounting", "Eric", 25)
print(t2)
print(t3)
Sample output
1 program hello world Eric 3
1: program hello world (3 hours), programmer Eric NOT FINISHED
False
1: program hello world (3 hours), programmer Eric FINISHED
True
2: program webstore (10 hours), programmer Adele NOT FINISHED
3: program mobile app for workload accounting (25 hours), programmer Eric NOT FINISHED
Some clarifications:

the state of the task (finished or not yet finished) can be checked with the function is_finished(self) which returns a Boolean value
a task is not finished when it is created
a task is marked as finished by calling the method mark_finished(self)
the id of a task is a running number which starts with 1. The id of the first task is 1, the id of the second is 2, and so forth.
Hint: id can be implemented as a class variable.

OrderBook

Please write a class named OrderBook which collects all the tasks ordered from the software company. The tasks should be modelled with the class Task you just wrote.

The basic version of an OrderBook is used as follows:

orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Eric", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)

for order in orders.all_orders():
    print(order)

print()

for programmer in orders.programmers():
    print(programmer)
Sample output
1: program webstore (10 hours), programmer Adele NOT FINISHED
2: program mobile app for workload accounting (25 hours), programmer Eric NOT FINISHED
3: program app for practising mathematics (100 hours), programmer Adele NOT FINISHED

Adele
Eric
At this stage your OrderBook should provide three methods:

add_order(self, description, programmer, workload) which adds a new order to the OrderBook. An OrderBook stores the orders internally as Task objects. NB: the method should take exactly the arguments mentioned, or else the automated tests will not work correctly.
all_orders(self) returns a list of all the tasks stored in the OrderBook
programmers(self) returns a list of the names of all the programmers with tasks stored in the OrderBook. The list should contain each programmer only once
Hint: an easy method for removing duplicates is handling the list initially as a set. A set is a collection of items where each unique item appears only once. A set can be then converted back into a list, and we can then be sure each item is now unique:

my_list = [1,1,3,6,4,1,3]
my_list2 = list(set(my_list))
print(my_list)
print(my_list2)
Sample output
[1, 1, 3, 6, 4, 1, 3]
[1, 3, 4, 6]
Some more features for OrderBook

Please write three more methods in your OrderBook class.

The method mark_finished(self, id: int) takes the id of the task as its argument and marks the relevant task as finished:

orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Eric", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)

orders.mark_finished(1)
orders.mark_finished(2)

for order in orders.all_orders():
    print(order)
Sample output
1: program webstore (10 hours), programmer Adele FINISHED
2: program mobile app for workload accounting (25 hours), programmer Eric FINISHED
3: program app for practising mathematics (100 hours), programmer Adele NOT FINISHED
If there is no task with the given id, the method should raise a ValueError exception. If you need a refresher on raising exceptions, please have a look at part 6.

The methods finished_orders(self) and unfinished_orders(self) work as expected: both return a list containing the relevant tasks from the OrderBook.

Finishing touches to OrderBook

Please write one last method in your OrderBook class: status_of_programmer(self, programmer: str) which returns a tuple. The tuple should contain the number of finished and unfinished tasks the programmer has assigned to them, along with the estimated hours in both categories.

orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Adele", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)
orders.add_order("program the next facebook", "Eric", 1000)

orders.mark_finished(1)
orders.mark_finished(2)

status = orders.status_of_programmer("Adele")
print(status)
Sample output
(2, 1, 35, 100)
The first item in the tuple is the number of finished tasks, while the second item is the number of unfinished tasks. The third and fourth items are the sums of workload estimates for the finished and unfinished tasks, respectively.

If there is no programmer with the given name, the method should raise a ValueError exception.
"""


# Write your solution here:
import uuid

class Task:
    idno = 1

    def __init__(self, description: str, programmer: str, workload: int):
        self.__id = Task.idno
        Task.idno += 1
        self.__description = description
        self.__programmer = programmer
        self.__workload = workload
        self.__finished = False

    def __str__(self):
        return f"{self.__id}: {self.__description} ({self.__workload} hours), programmer {self.__programmer} {'NOT FINISHED' if self.__finished == False else 'FINISHED'}"

    def is_finished(self):
        return self.__finished

    def mark_finished(self):
        self.__finished = True

    @property
    def id(self):
        return self.__id

    @property
    def description(self):
        return self.__description

    @property
    def programmer(self):
        return self.__programmer

    @property
    def workload(self):
        return self.__workload

class OrderBook:
    def __init__(self):
        self.__tasks = []
    
    def add_order(self, description, programmer, workload):
        self.__tasks.append(Task(description, programmer, workload))
    
    def all_orders(self):
        return self.__tasks
    
    def programmers(self):
        all_programmers = [task.programmer for task in self.__tasks]
        return list(set(all_programmers))

    def mark_finished(self, id):
        tasks = [task for task in self.all_orders() if task.id == id]

        if tasks:
            tasks[0].mark_finished()
        else:
            raise ValueError("No task with this id")

    def finished_orders(self):
        return [task for task in self.__tasks if task.is_finished()]

    def unfinished_orders(self):
        return [task for task in self.__tasks if not task.is_finished()]

    def status_of_programmer(self, programmer: str):
        finished = [task.workload for task in self.all_orders() if task.programmer == programmer and task.is_finished()]
        unfinished = [task.workload for task in self.all_orders() if task.programmer == programmer and not task.is_finished()]

        if finished or unfinished:
            return (len(finished), len(unfinished), sum(finished), sum(unfinished))
        else:
            raise ValueError("No programmer with this name")



if __name__ == "__main__":
    ##Part 1: Task
    # t1 = Task("program hello world", "Eric", 3)
    # print(t1.id, t1.description, t1.programmer, t1.workload)
    # print(t1)
    # print(t1.is_finished())
    # t1.mark_finished()
    # print(t1)
    # print(t1.is_finished())
    # t2 = Task("program webstore", "Adele", 10)
    # t3 = Task("program mobile app for workload accounting", "Eric", 25)
    # print(t2)
    # print(t3)

    ##Part 2: OrderBook
    # orders = OrderBook()
    # orders.add_order("program webstore", "Adele", 10)
    # orders.add_order("program mobile app for workload accounting", "Eric", 25)
    # orders.add_order("program app for practising mathematics", "Adele", 100)

    # for order in orders.all_orders():
    #     print(order)

    # print()

    # for programmer in orders.programmers():
    #     print(programmer)

    ##Part3: Some more features for OrderBook
    # orders = OrderBook()
    # orders.add_order("program webstore", "Adele", 10)
    # orders.add_order("program mobile app for workload accounting", "Eric", 25)
    # orders.add_order("program app for practising mathematics", "Adele", 100)

    # orders.mark_finished(1)
    # orders.mark_finished(2)

    # for order in orders.all_orders():
    #     print(order)

    # print()

    # for order in orders.finished_orders():
    #     print(order)

    # print()

    # for order in orders.unfinished_orders():
    #     print(order)

    # ##Part4: Finishing touches to OrderBook
    # orders = OrderBook()
    # orders.add_order("program webstore", "Adele", 10)
    # orders.add_order("program mobile app for workload accounting", "Adele", 25)
    # orders.add_order("program app for practising mathematics", "Adele", 100)
    # orders.add_order("program the next facebook", "Eric", 1000)

    # orders.mark_finished(1)
    # orders.mark_finished(2)

    # status = orders.status_of_programmer("Adele")
    # print(status)

    t = OrderBook()
    t.add_order("program web store", "Andy", 10)
    t.add_order("program mobile gane", "Eric", 5)
    t.mark_finished(1)
    t.mark_finished(2)
    for order in t.all_orders():
        print(order)

"""
#Suggested solution

class Task:
    id = 0
    @classmethod 
    def new_id(cls):
        Task.id += 1
        return Task.id
 
    def __init__(self, description, programmer, workload):
        self.programmer = programmer
        self.description = description
        self.workload = workload
        self.id = Task.new_id()
        self.finished = False
    
    def is_finished(self):
        return self.finished 
 
    def mark_finished(self):
        self.finished = True
 
    def __str__(self):
        status = "NOT FINISHED" if not self.finished else "FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"
 
class OrderBook:
    def __init__(self):
        self.__tasks = []
 
    def add_order(self, description, programmer, workload):
        self.__tasks.append(Task(description, programmer, workload))
 
    def all_orders(self):
        return self.__tasks
 
    def programmers(self):
        return list(set([t.programmer for t in self.__tasks]))
 
    def mark_finished(self, id: int):
        for task in self.__tasks:
            if task.id == id:
                task.mark_finished()
                return
        
        # not incorrect
        raise ValueError("wrong id")
    
    def unfinished_orders(self):
        return [t for t in self.__tasks if not t.is_finished()]
 
    def finished_orders(self):
        return [t for t in self.__tasks if t.is_finished()]
 
    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError("Programmer does not exists")
        
        finished_tasks = [t for t in self.__tasks if t.programmer == programmer and t.is_finished() ]
        not_finished_tasks = [t for t in self.__tasks if t.programmer == programmer and not t.is_finished() ]
 
        finished_hours = sum(t.workload for t in finished_tasks)
        not_finished_hours = sum(t.workload for t in not_finished_tasks)
 
        return (len(finished_tasks), len(not_finished_tasks), finished_hours, not_finished_hours)
# Write your solution here:
    
#Review
My solution results in the same output, the suggested one works a bit
differently as doesn't use len() method to count the subordinates. 
"""
    


    



    