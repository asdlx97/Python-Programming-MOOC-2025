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
