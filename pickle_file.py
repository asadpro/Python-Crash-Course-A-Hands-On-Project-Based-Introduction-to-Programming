import pickle
from pickletools import optimize
import sys
import bz2

dictionary = {
    "name": "asadpro",
    "father_name": "habib",
    "address": "Dalazak road",
}
listofNumbers = [1, 2, 3, 4, 5, 6]
filename = "pickle_file.pkl"
filename2 = "binary_file.txt"

# infile = open(filename, "wb")  # Pickle file can be stored into two mode 'wb', 'rb'
# pickle.dump(dictionary, infile)
# infile.close()

# # De-serializing the above file.
# outfile = open(filename, "rb")
# read_pickle = pickle.load(outfile)
# size = sys.getsizeof(read_pickle)
# print("Before compression size in bytes: ", size)
# outfile.close()

# 🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨

# filename2 = "compressPickle.txt"
# # Here below we have created a compress file
# sfile = bz2.BZ2File(filename2, "wb")
# pickle.dump(dictionary, sfile)
# sfile.close()

# # Below we have read the above compressed file.
# sfile_read = bz2.BZ2File(filename2, "rb")
# content = pickle.load(sfile_read)
# sizeofCompress = sys.getsizeof(content)
# print("After compression size in bytes: ", sizeofCompress)
# sfile_read.close()

# 🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨
# writing and reading of a pickle file using with keyword
# with open(filename2, "wb") as file_write:
#     pickle.dump(dictionary, file_write)

# # before reading the file open it manually but it will not open because it's in binary format with the following method you can read binary files.

# with open(filename2, "rb") as file_read:
#     content = pickle.load(file_read)
#     print(content)


# 🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯
# Using json module
# import json
# import requests

# api = "https://api.openweathermap.org/data/2.5/weather?lat=34.008000&lon=71.578490&appid=3d6d8ca187e1d7e3828c4ba2092b61f9"

# json_file = "jsonfile.json"
# content = requests.get(api)
# content_text = content.text

# with open(json_file, "w") as json_object:
#     json.dump(content_text, json_object)

# with open(json_file, "r") as json_object_read:
#     readfile = json.load(json_object_read)
#     print(readfile)

# 🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯🧯
# Converting jpg image to png image using python

from PIL import Image

# im1 = Image.open("C:\\Users\\User\\Downloads\\transcript.jpg")
# im1.save("C:\\Users\\User\\Downloads\\transcript_BSCS.png")


# # Resizing the above image using pil library
# new_image = im1.resize([1080, 1280])
# new_image.save("C:\\Users\\User\\Downloads\\transcript_resize.png")
# print(new_image.size)


# 🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉

# Resize the size of provisional certificate and degree.

# provisional = Image.open("C:\\Users\\User\\Downloads\\provisional.jpg")
# new_provisional = provisional.resize([1080, 1280])
# new_provisional.save("C:\\Users\\User\\Downloads\\provisional_certificate.png")

# Degree resize
# degree = Image.open("C:\\Users\\User\\Downloads\\degree_certificate.png")
# new_degree = degree.resize([1280, 920])
# new_degree.save("C:\\Users\\User\\Downloads\\degree_certificate.pdf")


class A:
    def displayA(self):
        print("This is class A")


class B:
    def display(self):
        print("This is class B")


class C(A, B):
    def display(self):
        print("This is class C")


object_C = C()
object_d = B()

# Below both of the displays method will take the same address space on memory.
print(id(object_C.display()) == id(object_d.display()))

print(id(object_C.display()))
print(id(object_d.display()))
