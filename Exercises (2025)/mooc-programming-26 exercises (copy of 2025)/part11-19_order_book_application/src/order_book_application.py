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

