def removeSJW(mystring):
    string=mystring.split(" ")
    if string[0]=="SJW":
        return mystring
    else:
     return mystring.replace("SJW","") 

# expected output: WGU Rocks
print(removeSJW('SJW is term used to describe a generation of people who like to scream at their mom in Walmart.'))
# expected output: Hello, John
print(removeSJW('Wouldnt it be niceSJW if we could remove the word completely, SJWit seems to sneakSJW in wherever it can, only to contaminate logical discourse and adult SJWconversations.'))