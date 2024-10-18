import tkinter as tk  # Ensure Tkinter is imported

# Initialize the main application window
root = tk.Tk()
root.title("Calculator")
root.geometry('350x460')
root.resizable(0, 0)
root.configure(bg='black')

# Variables for first number, second number, operator, and memory
fnum = sec_num = operator = None
memory_value = 0

# Function to handle operator input
def getop(op):
    global fnum, operator
    fnum = float(result_label['text']) if result_label['text'] else 0
    operator = op
    clr()

# Function to display the number or decimal point pressed
def print_text(s):
    current = result_label['text']
    if current == 'Error':
        current = ''
    new = current + str(s)
    result_label.config(text=new)

# Function to clear the display
def clr():
    result_label.config(text='')

# Function to calculate the result
def result():
    global fnum, operator, sec_num
    sec_num = float(result_label['text']) if result_label['text'] else 0

    if operator == '+':
        result_label.config(text=str(fnum + sec_num))
    elif operator == '-':
        result_label.config(text=str(fnum - sec_num))
    elif operator == '*':
        result_label.config(text=str(fnum * sec_num))
    elif operator == '/':
        if sec_num == 0:
            result_label.config(text='Error')
        else:
            result_label.config(text=str(round(fnum / sec_num, 2)))

# Memory functions
def memory_store():
    global memory_value
    memory_value = float(result_label['text']) if result_label['text'] else 0
    clr()

def memory_recall():
    result_label.config(text=str(memory_value))

# Create and configure the display label
result_label = tk.Label(root, text='', bg='black', fg='white')
result_label.grid(row=0, column=0, pady=(40, 20), columnspan=6, sticky='w')
result_label.config(font=('verdana', 30, 'bold'))

# Number buttons
btns = [
    ('7', 4, 0), ('8', 4, 1), ('9', 4, 2),
    ('4', 5, 0), ('5', 5, 1), ('6', 5, 2),
    ('1', 6, 0), ('2', 6, 1), ('3', 6, 2),
    ('0', 7, 1), ('.', 7, 0)  # Added decimal button
]

for (text, row, col) in btns:
    btn = tk.Button(root, text=text, bg='green', fg='white', width=7, height=3,
                    command=lambda t=text: print_text(t))
    btn.grid(row=row, column=col)
    btn.config(font=('verdana', 14, 'bold'))

# Operator buttons
operators = [
    ('+', 4, 3), ('-', 5, 3),
    ('*', 6, 3), ('/', 7, 3)
]

for (text, row, col) in operators:
    btn = tk.Button(root, text=text, fg='white', bg='green', width=7, height=3,
                    command=lambda t=text: getop(t))
    btn.grid(row=row, column=col)
    btn.config(font=('verdana', 14, 'bold'))

# Other buttons for equals, clear, and memory functions
btn_eq = tk.Button(root, text='=', fg='white', bg='green', width=7, height=3, command=result)
btn_eq.grid(row=7, column=2)
btn_eq.config(font=('verdana', 14, 'bold'))

btn_clr = tk.Button(root, text='C', fg='white', bg='green', width=7, height=3, command=clr)
btn_clr.grid(row=7, column=0)
btn_clr.config(font=('verdana', 14, 'bold'))

btn_m_store = tk.Button(root, text='M+', fg='white', bg='green', width=7, height=3, command=memory_store)
btn_m_store.grid(row=8, column=0)
btn_m_store.config(font=('verdana', 14, 'bold'))

btn_m_recall = tk.Button(root, text='MR', fg='white', bg='green', width=7, height=3, command=memory_recall)
btn_m_recall.grid(row=8, column=1)
btn_m_recall.config(font=('verdana', 14, 'bold'))

# Run the application
root.mainloop()
