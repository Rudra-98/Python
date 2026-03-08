
with open('sample_text.txt','r') as file:
    content = file.read()
    print(content)

#read line by line
with open('sample_text.txt','r') as file:
    for line in file:
        print(line.strip())


#read line by line
with open('sample_text.txt','w') as file:
    file.write("Hello World\n")
    file.write("How are you doing?")



#write without overriding the file using append mode
with open('sample_text.txt','a') as file:
    file.write("\nwhat is today\n")
    file.write("what is tomorrow\n")


#writing lines to the file
lines = ['first line\n','second line\n','third line\n']
with open('sample_text.txt','a') as file:
    file.writelines(lines)


#writing to the binary file
data = b'\x01\x02\x03\x04'
with open('sample_bin.bin','wb') as file:
    file.write(data)



with open('sample_bin.bin','rb') as file:
    contents = file.read()
    print(contents)










