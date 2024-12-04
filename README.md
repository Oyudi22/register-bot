# Register Automation

This automation bot is built in Python, using PyAutoGUI and Time, including employees in the system, colecting all informations for the e-mail creation.
The program initialize by reading an especific archive, .txt in this case, with the `open()` function.

It starts by reading the informations separated by ',' and saves as 'file'.
`with open('name.txt', 'r', encoding="UTF-8") as file:`

In this .txt file, all informations are formatted by the following:
`Nome, MiddleName, LastName, ID`

Storing information in file, a for loop is called to ends when all e-mails are made.
`for line in file:`

Before the program starts registering, it defines 5 variables: Name, MiddleName, LastName, Identification and Password.
Within all variables, the function split() is used to separate each information before the especified character and it stores to each variable defined with an Index.
Example:
`name = line.split(',')[0]`
So:
```
name = line.split(',')[0]
middleName = line.split(',')[1]
lastName = line.split(',')[2]
id = line.split(',')[3]
pswd = 12345678
```

From this definition, "code blocks" are separated by each function, like: Register selection, Write the Name and MiddleName, Last Name,
Formatting the e-mail, Selecting the position, Creating a temporary password, Finishing, Selecting, Copying and pasting in a another file,
and jumping to the next line.

With this bot, it was possible to register more than 100 intern in less than 30 minutes, which could take 2 hours to make by hand
