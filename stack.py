
class StackError(Exception):
    pass


class Stack(object):
    """
    Class representing the Stack data structure.
    A stack is a linear data structure in which insertions and
    deletions are performed only at one end. Hence it is called
    Last In First Out(LIFO) data structure.
    Eg: A stack of plates in a restaurant.
    """

    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size

    def push(self, value):
        if len(self.items) >= self.max_size:
            raise StackError('StackOverflow!!!!')
        self.items.append(value)

    def pop(self):
        if not self.items:
            raise StackError('StackUnderflow!!!')
        return self.items.pop()

    def size(self):
        return len(self.items)

    def print_stack(self):
        if not self.items:
            print('Stack is empty')
            return
        for i in self.items:
            print(i, end=', ')
        print()


def main():
    max_size = int(input('Enter the size of the stack: '))
    s = Stack(max_size)
    while True:
        try:
            s.print_stack()
            print('0. Exit\n1. Push\n2. Pop\n')
            choice = int(input('Enter your choice: '))
            if choice == 0:
                break
            elif choice == 1:
                value = int(input('Enter the value to be inserted: '))
                s.push(value)
            elif choice == 2:
                print('Poped value is {}'.format(s.pop()))
            else:
                print('Wrong Choice')
        except StackError as e:
            print(e)


if __name__ == '__main__':
    main()
