"""
1. Create a text file named emails.txt containing multiple email addresses, some in uppercase and some repeated.
Write a Python program to clean the data by converting all emails to lowercase, removing duplicates, sorting them alphabetically, and saving the cleaned list to a new file named unique_emails.txt.


2. Create a text file named names.txt containing a list of names.
Some names may have extra spaces, inconsistent capitalization (like “aLiCe” or “ bob ”), or appear more than once.
Write a Python program to clean the data by:
  1.  Removing extra spaces.
  2.  Converting all names so that only the first letter is capitalized.
  3.  Removing duplicate names. 
  4. Sorting the names alphabetically.
  Finally, save the cleaned list into a new file named clean_names.txt.


3. Write a Python program that creates a list of 5 numbers.
Ask the user for an index number and print the value at that index.
If the index is out of range, handle the exception and print "Invalid index!".


"""

# 1 solution
with open("./sample_data/emails.txt","w+") as file:
  file.write("swaron3214@gmail.com\n")
  file.write("Swaron3214@gmail.com\n")
  file.write("redWan@gmail.com\n")
  file.write("app32144851@Gmail.com\n")
  file.write("eswaron223418@bscse.uiu.ac.bd\n")
  file.write("IBNUL@gmAIL.COM\n")


try:
  with open("./sample_data/emails.txt","r") as file:
    emails = list(map(str.strip,file))
    emails = list(map(lambda x : x.lower(), emails))
    emails = set(emails)
    emails = list(emails)
    emails = sorted(emails)

  with open("./sample_data/unique_emails.txt","w") as file:
    file.write("\n".join(emails))

except Exception as e:
  print(e)







"""

Problem 5: Write and Read a File
Problem:
 Write a Python program to:
Create a text file named data.txt


Write “Learning Python is fun!” into it.


Read the file and print its content.

"""

try:  
  with open("./sample_data/data.txt","w+") as file:
    file.write("Learning Python is fun!")
    # print(file.tell())
    file.seek(0)
    content = file.read()
    print(content)
except Exception as e:
  print(e)