from collections import deque

"""
Вопрос №2

На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой 
реализации.

Оценивается:
1. Полнота и качество реализации
2. Оформление кода
3. Наличие сравнения и пояснения по быстродействию
"""

"""Честно говоря, первый раз работаю с буферами и конкретно пояснить за производительность не могу, но судя по тому 
материалу что я изучил при решении поставленной задачи скорость работы приблизительно ровна, однако отмечают, 
что скорость работы буфера, основанного на обычном списке незначительно быстрее, однако скорее всего это зависит от 
места применения буфера.

Суть работы буфера я понял, однако пока не совсем понимаю, где и как его применяют (изучу этот вопрос).
"""


class Fifo_deque:
    def __init__(self, max_len_buffer: int):
        self.max_len_buffer = max_len_buffer
        self.buffer = deque(maxlen=max_len_buffer)

    def push(self, item):
        if len(self.buffer) == self.max_len_buffer:
            raise Exception('Buffer is full')
        self.buffer.append(item)

    def pop(self):
        if self.buffer:
            return self.buffer.popleft()
        else:
            raise Exception(f'No elements in buffer!')


class Fifo_list:
    def __init__(self, max_len_buffer: int):
        self.capacity = max_len_buffer
        self.buffer = [None] * max_len_buffer
        self.head = 0
        self.tail = 0
        self.size = 0

    def push(self, item):
        if self.size == self.capacity:
            raise Exception('Buffer is full')
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise Exception('No elements in buffer!')
        item = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item


if __name__ == "__main__":

    q = Fifo_deque(10)
    for i in range(10):
        q.push(i)

    for _ in range(10):
        print(q.pop())

    q2 = Fifo_list(10)
    for i in range(10):
        q.push(i)

    for _ in range(10):
        print(q.pop())
