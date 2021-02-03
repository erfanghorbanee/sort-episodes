import os
import fnmatch
import shutil

directory = input("enter your directory: ")

''' for pattern input the same word in all files.
 if there is other characters before or after the pattern use *
 for example: *pattern* '''
pattern = input("enter the pattern: ")


def find_match():
    i = 0
    try:
        for file_name in os.listdir(directory):
            if fnmatch.fnmatch(file_name.lower().replace(" ", "."),
                               pattern.lower().replace(" ", ".")):

                i += 1

                # creating the destination folders
                dst = os.path.join(directory, str(i))
                os.makedirs(dst)

                src = os.path.join(directory, file_name)
                # moving the source files to the destination folders
                shutil.move(src, dst)
        print("The operation was successful :)")

    except:
        print("The operation was unsuccessful")


find_match()
