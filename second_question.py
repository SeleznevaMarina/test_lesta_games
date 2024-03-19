# Класс Queue - связная очередь, построенная из связанных объектов Node.
# Извлекаемый из очереди элемент, который был добавлен первым.
# Метод remove с постоянным временем выполнения, тк в нем нет циклов, вызовов функций и тп
# Метод insert с линейным временем выполнения, тк необходимо пройти весь список,
# чтобы найти последний элемент, это сильно затратно
class Queue:
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return (self.length == 0)

    def insert(self, cargo):
        node = Node(cargo)
        node.next = None
        if self.head == None:
            # если список пуст, новый элемент идет первым
            self.head = node
        else:
            # находим последний элемент в списке
            last = self.head
            while last.next: last = last.next
            # добавляем новый
            last.next = node
        self.length += 1

    def remove(self):
        if self.length == 0:
            return
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        return cargo
# Класс PriorityQueue - приоритетная очередь.
# Oтличие состоит в том, что извлекаемый из очереди элемент не обязательно тот,
# который был добавлен в очередь первым, а тот, у которого наивысший приоритет.
# В каждой итерации элемент сравнивается с maxi (элемент с наивысшим приоритетом).
# Посе завершения цикла for maxi содержит самый приоритетный элемент.
class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]: maxi = i
        item = self.items[maxi]
        self.items[maxi:maxi+1] = []
        return item
    