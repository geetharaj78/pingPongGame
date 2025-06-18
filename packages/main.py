from prettytable import PrettyTable
table = PrettyTable()
table.add_column("characteristics of the person",["lazy","funny","witty"])
table.add_column("good/bad",["good","bad","good"])
table.align = "l"
print(table)
