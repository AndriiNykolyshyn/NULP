import tkinter as tk
from functools import partial

class View:

    def __init__(self):
        self.window = tk.Tk()

    def init_components(self):
        self.init_output_label()
        self.init_number_buttons()
        self.init_clear_button()
        self.init_equal_button()
        self.init_operation_buttons()

    def number_event(self, value):
        print('view:number_event: ' + str(value))

    def clear_event(self):
        print('view:clear_event')

    def equal_event(self):
        print('view:equal_event')

    def operation_event(self, value):
        print('view:operation_event: ' + str(value))

    def set_output(self, value):
        print('view:set_output: ' +str(value))
        self.output.set(str(value))

    def init_number_buttons(self):
        row = 0
        column = 0

        for num in range(10):
            button = tk.Button(self.window, text=str(num), command=partial(self.number_event, num))

            if num % 3 == 0:
                row += 1
                column = 0
            else:
                column += 1

            button.grid(row=row, column=column)

    def init_clear_button(self):
        button = tk.Button(self.window, text="C", command=self.clear_event)
        button.grid(row=4, column=1)

    def init_equal_button(self):
        button = tk.Button(self.window, text="=", command=self.equal_event)
        button.grid(row=4, column=2)

    def init_output_label(self):
        self.output = tk.StringVar()
        self.output_label = tk.Label(self.window, textvariable=self.output, relief=tk.RAISED)
        self.output.set(str(0))
        self.output_label.grid(row=0, column=0, columnspan=10)

    def init_operation_buttons(self):
        add_button = tk.Button(self.window, text="+", command=partial(self.operation_event, 1))
        add_button.grid(row=1, column=3)

        subtract_button = tk.Button(self.window, text="-", command=partial(self.operation_event, 2))
        subtract_button.grid(row=2, column=3)

        multiply_button = tk.Button(self.window, text="*", command=partial(self.operation_event, 3))
        multiply_button.grid(row=3, column=3)

        divide_button = tk.Button(self.window, text="/", command=partial(self.operation_event, 4))
        divide_button.grid(row=4, column=3)

class Calculate:
    def __init__(self):
        self.__result = 0
        self.__number = 0
        self.__operation = Operation.none

    def add(self):
        self.__result += self.__number

    def subtract(self):
        self.__result -= self.__number

    def multiply(self):
        self.__result *= self.__number

    def divide(self):
        self.__result /= self.__number

    def append(self, value):
        if self.__operation == Operation.none:
            self.__result = int(str(self.__result) + str(value))
            self.set_output(self.__result)
        else:
            self.__number = int(str(self.__number) + str(value))
            self.set_output(self.__number)

    def set_operation(self, value):
        self.__operation = Operation(value)

    def do_operation(self):
        if self.__operation == Operation.add:
            self.add()
        elif self.__operation == Operation.subtract:
            self.subtract()
        elif self.__operation == Operation.multiply:
            self.multiply()
        elif self.__operation == Operation.divide:
            self.divide()

        self.__number = 0

        self.set_output(self.__result)

    def get_result(self):
        return self.__result

    def clear(self):
        self.__result = 0
        self.__number = 0
        self.__operation == Operation.none
        self.set_output(0)

    def set_output(self, value):
        print('calc:set_output: ' + str(value))

from enum import Enum

class Operation(Enum):
    none = 0
    add = 1
    subtract = 2
    multiply = 3
    divide = 4

view = View()
calc = Calculate()
    
calc.set_output = view.set_output

view.number_event = calc.append
view.clear_event = calc.clear
view.operation_event = calc.set_operation
view.equal_event = calc.do_operation

view.init_components()

view.window.mainloop()
