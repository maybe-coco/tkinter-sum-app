import tkinter as tk

#Making Function
def number_sum():
    #Taking value from Entry box
    n1 = entry_one.get()
    n2 = entry_two.get()

    result = float(n1) + float(n2)
    #Adding result in result_label
    result_label.config(text="The sum is : " + str(result))

#Making main window
root = tk.Tk()
root.title("Sum of two numbers")
root.geometry("550x300")
root.configure(bg="blue")

#1st number's label and entry
label_one = tk.Label(root, text="<Enter first number>", font=("consolas",15),bg="gray",fg="black")
label_one.pack()
entry_one = tk.Entry(root, bg="green", fg="white",font=("consolas",15))
entry_one.pack()

#1st number's label and entry
label_two = tk.Label(root, text="<Enter second number>", font=("consolas",15),bg="gray",fg="black")
label_two.pack()
entry_two = tk.Entry(root, bg="green", fg="white",font=("consolas",15))
entry_two.pack()

#Making Calculate Button
calculate_button = tk.Button(root, text="Calculate Sum", height=3, width=14, bg="red", fg="yellow", command=number_sum)
calculate_button.pack()

#Result's label
result_label = tk.Label(root, bg="orange", fg="green", font=("consolas",15), text="The sum is : ")
result_label.pack()
root.mainloop()  