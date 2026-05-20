"""
NB: Some exercises have multiple parts, and you can receive points for the different parts separately. You can submit a partially completed exercise by choosing 'Submit Solution' from the menu next to the button for executing tests .

In this exercise you will create an interactive application for administering the tasks ordered from a software company. The implementation is completely up to you, but you may use the building blocks from the previous exercise in your application. The examples in the last section of part 10 can also prove useful.

Without error handling

The application should work exactly as follows:

Sample output
commands:
0 exit
1 add order
2 list finished tasks
3 list unfinished tasks
4 mark task as finished
5 programmers
6 status of programmer

command: 1
description: program the next facebook
programmer and workload estimate: jonah 1000
added!

command: 1
description: program mobile app for workload accounting
programmer and workload estimate: eric 25
added!

command: 1
description: program an app for music theory revision
programmer and workload estimate: nina 12
added!

command: 1
description: program the next twitter
programmer and workload estimate: jonah 55
added!

command: 2
no finished tasks

command: 3
1: program the next facebook (1000 hours), programmer jonah NOT FINISHED
2: program mobile app for workload accounting (25 hours), programmer eric NOT FINISHED
3: program an app for music theory revision (12 hours), programmer nina NOT FINISHED
4: program the next twitter (55 hours), programmer jonah NOT FINISHED

command: 4
id: 2
marked as finished

command: 4
id: 4
marked as finished

command: 2
2: program mobile app for workload accounting (25 hours), programmer eric FINISHED
4: program the next twitter (55 hours), programmer jonah FINISHED

command: 3
1: program the next facebook (1000 hours), programmer jonah NOT FINISHED
3: program an app for music theory revision (12 hours), programmer nina NOT FINISHED

command: 5
jonah
eric
nina

command: 6
programmer: jonah
tasks: finished 1 not finished 1, hours: done 55 scheduled 1000
The first exercise point is granted for a working application when all user input is flawless.

Handling errors in user input

To gain the second exercise point for this exercise your application is expected to recover from erroneus user input. Any input which does not follow the specified format should produce an error message erroneous input, and result in yet another repeat of the loop asking for a new command:

Sample output
command: 1
description: program mobile app for workload accounting
programmer and workload estimate: eric xxx
erroneous input

command: 1
description: program mobile app for workload accounting
programmer and workload estimate: eric
erroneous input

command: 4
id: 1000000
erroneous input

command: 4
id: XXXX
erroneous input

command: 6
programmer: unknownprogrammer
erroneous input
"""


# Write your solution here
# If you use the classes made in the previous exercise, copy them here
# Write your solution here:
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
    
    def add_order(self, description: str, programmer: str, workload: str):
        self.__tasks.append(Task(description, programmer, workload))
    
    def all_orders(self):
        return self.__tasks
    
    def programmers(self):
        all_programmers = [task.programmer for task in self.__tasks]
        return list(set(all_programmers))

    def mark_finished(self, id):
        tasks = [order for order in self.__tasks if order.id == id]

        if tasks:
            tasks[0].mark_finished()
        else:
            raise ValueError("No task with this id")

    def finished_orders(self):
        orders = [task for task in self.__tasks if task.is_finished()]

        if not orders:
            return None
        else:
            return orders

    def unfinished_orders(self):
        orders = [task for task in self.__tasks if not task.is_finished()]

        if not orders:
            return None
        else:
            return orders

    def status_of_programmer(self, programmer: str):
        finished = [task.workload for task in self.all_orders() if task.programmer == programmer and task.is_finished()]
        unfinished = [task.workload for task in self.all_orders() if task.programmer == programmer and not task.is_finished()]

        if finished or unfinished:
            return (len(finished), len(unfinished), sum(finished), sum(unfinished))
        else:
            raise ValueError("No programmer with this name")

class OrderApplication:
    def __init__(self):
        self.__orderbook = OrderBook()

    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")
        print()

    def add_order(self):
        try:
            description = input("description: ")
            programmer, workload = input("programmer and workload: ").split()
            workload = int(workload)
            self.__orderbook.add_order(description, programmer, workload)
            print("added!\n")
        except:
            print("erroneous input\n")
        
    def finished_orders(self):
        if self.__orderbook.finished_orders() == None:
            print("no finished tasks")
        else:
            for order in self.__orderbook.finished_orders():
                print(order)
        print()

    def unfinished_orders(self):
        if self.__orderbook.unfinished_orders() == None:
            print("no unfinished tasks")
        else:
            for order in self.__orderbook.unfinished_orders():
                print(order)
        print()

    def mark_finished(self):
        try:
            id = int(input("id: "))
            self.__orderbook.mark_finished(id)
            print("marked as finished\n")
        except ValueError:
            print("erroneous input\n")


    def programmers(self):
        for programmer in self.__orderbook.programmers():
            print(programmer)
        print()

    def status_programmer(self):
        try:
            name = input("programmer: ")

            status = self.__orderbook.status_of_programmer(name)
            print(f"tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}\n")
        except ValueError:
            print("erroneous input\n")
        
    def execute(self):
        self.help()

        while True:
            choice = input("command: ")
            if choice == "0":
                break
            if choice == "1":
                self.add_order()
            if choice == "2":
                self.finished_orders()
            if choice == "3":
                self.unfinished_orders()
            if choice == "4":
                self.mark_finished()
            if choice == "5":
                self.programmers()
            if choice == "6":
                self.status_programmer()


app = OrderApplication()
app.execute()


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
 
class Application:
    def __init__(self):
        self.orders = OrderBook()
 
    def instructions(self):
        # Defining multiline string is possible with triple apostrophes
        instructions_str = """
commands:
0 exit
1 add order
2 list finished tasks
3 list unfinished tasks
4 mark task as finished
5 programmers
6 status of programmer"""
        print(instructions_str)
 
    def add(self):
        description = input("description: ")
        programmer_and_estimate = input("programmer and workload estimate: ")
        try:
            programmer = programmer_and_estimate.split(' ')[0]
            workload = int(programmer_and_estimate.split(' ')[1])
            self.orders.add_order(description, programmer, workload)
            print("added!")
        except:
            print("erroneous input")
 
    def unfinished(self):
        for task in self.orders.unfinished_orders():
            print(task)
 
    def finished(self):
        finished_orders = self.orders.finished_orders()
        if len(finished_orders)==0:
            print("no finished tasks")
            return
 
        for task in finished_orders:
            print(task)
 
    def programmers(self):
        for programmer in self.orders.programmers():
            print(programmer)
 
    def mark_finished(self):
        try:
            order_id = int(input("id: "))
            self.orders.mark_finished(order_id)
            print("marked as finished")
        except:
            print("erroneous input")
 
    def programmers_status(self):
        programmer = input("programmer: ")
        if not programmer in self.orders.programmers():
            print("erroneous input")
            return
 
        status = self.orders.status_of_programmer(programmer)
        print(f"tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}")
 
    def run(self):
        self.instructions()
        while True:
            command = input("command: ")
            if command == "0":
                return
            elif command == "1":
                self.add()
            elif command == "2":
                self.finished()
            elif command == "3":
                self.unfinished()
            elif command == "4":
                self.mark_finished()
            elif command == "5":
                self.programmers()
            elif command == "6":
                self.programmers_status()
            print()
 
Application().run()
    
#Review
My solution results in the same output, the suggested one mostly
works the same way regarding the interface with try and except altough I
work with specific exceptions. 
"""