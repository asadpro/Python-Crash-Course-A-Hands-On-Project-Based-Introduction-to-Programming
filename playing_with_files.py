# Creating table from 2-20 and then save them to a separate .txt. file
# tables = [tab for tab in range(2,21)]

# def make_table(table_no):
#     store = ''
#     for j in range(1,11):
#         store += f'{table_no} x {j} = {table_no*j}\n'
#     store += '\n########################################## \n'
#     return store

# for table in tables:
#     save_table = make_table(table)
#     with open('tables.txt', 'a') as file:
#         file.write(save_table)

# with open('tables.txt', 'r') as read_file:
#     see_tables = read_file.read()
#     print(see_tables)


# 🌎🌎🌎🌎🌎 A file contain 'donkey' replace it with ###### in the same file. 🌎🌎🌎🌎🌎


# file = open('abusive_words.txt', 'r')
# rd = file.read()
# file.close()

# if "donkey" in rd:
#     with open('abusive_words.txt', 'w') as file:
#         file.write(rd.replace('donkey','#####'))


# file = open('abusive_words.txt', 'r')
# print(file.read())
# file.close()


# 🌎🌎🌎🌎🌎 Mine a log file and print out whether it contain 'python' or not. if yes then find it's line no 🌎🌎🌎🌎🌎
# content = True
# line_numbers = []
# counter = 0
# i = 0
# with open("log.txt", "r") as read_log:
#     while content:
#         i += 1  
#         content = read_log.readline()
#         if "python" in content:
#             line_numbers.append(i)
#             counter +=1
            
#     print(f'Python words exist in file {counter} times.')
#     for line in line_numbers:
#         print('Python on line no: ',line)


# 🌎🌎🌎🌎🌎 Copy one file content into other file and check whether content of both are identical or not. 🌎🌎🌎🌎🌎

# with open('abusive_words.txt', 'r') as read_file:
#     content = read_file.read()

# # Copying of one file content into other.
# with open('abusive_words_duplicate.txt' , 'w') as write_file:
#     write_file.write(content)

# # To check whether both are identical or not.
# with open('abusive_words.txt','r') as file1:
#     file1.read()
# with open('abusive_words_duplicate.txt','r') as file2:
#     file2.read()

# print(file1 == file2)

# 🌎🌎🌎🌎🌎 Write a program to wipe out the content of a file. 🌎🌎🌎🌎🌎
# with open('abusive_words.txt', 'w') as write_file:  
#     write_file.write('')
# with open('abusive_words.txt', 'r') as read_file:
#     content = read_file.read()
#     if content == '':
#         print('Content of the file is empty.')
#     else:
#         print("File is full of content")

class Car:
    def __init__(self):
        self.name = 'asad'
    
    def info(self):
        'Name of the employee: ',self.name

    # Creating a static method will not give error of 'self' keyword

    @staticmethod
    def great():
        print('You are great ')

car = Car()
save = car.info
print(car.info())
print(type(car.info()))
        
car.great()
