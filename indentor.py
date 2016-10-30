#!/usr/bin/python2

#opening the file as input_file object
with open("raw.txt") as input_file:
    #text contains all the text read from the file
    text = input_file.read()

#using this list as a stack
istack = []
str_length = 0
#this will contain the indentation level
indent = 0
current_string = ""

#removing the next line escape character from text
text = text.replace("\n{", "{")
#iterating for a single character in text
for char in text:
    #when the next line is encountered
    if char == '\n':
        print current_string
        #adding the appropriate no of indentation spaces
        current_string = " " * indent
        #setting up the string length to zero
        str_length = 0
    #if not of any of these characters - {,},[,],','
    elif not (char == '{' or char == '}' or char == '[' or char == ']' or char == ','):
        #append the character to current string and increment the string length
        str_length += 1
        current_string += char
    #if encountered the closing braces
    elif char == '}' or char == ']':
        #print the string with appropriate indentation level
        print current_string
        current_string = " " * indent
        print current_string + char
        #pop out the indentation from top of the stack
        indent = istack.pop()
        #apply it to current string
        current_string = " " * indent
        str_length = 0
    #if encountered the opening braces
    elif char == '{' or char == '[':
        #push the current indentation level to istack
        istack.append(indent)
        #current indentation level will contain sum of string length and top of stack
        indent = str_length + istack[-1]
        #print the string with appropriate indentation level
        print current_string + char
        current_string = " " * indent
        str_length = 0
    #if encountered ',' comma seperator
    elif char == ',':
        #print with current indentation level
        print current_string + char
        current_string = " " * indent
        str_length = 0
