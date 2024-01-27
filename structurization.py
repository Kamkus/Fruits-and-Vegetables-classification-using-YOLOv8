import os 



def productName(tekst):
    for znak in tekst:
        if znak.isdigit():
            return tekst[:tekst.index(znak)].strip()
    return None




createdDirectories = []


curDir = os.getcwd().replace('stucturization.py', "")


directory = curDir + '/old_data/val/images'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        product = productName(filename).replace("--", '')
        if not os.path.isdir(curDir + '/new_data/val/' + product):
            os.mkdir(curDir + '/new_data/val/' + product) 
        os.replace(f, curDir + '/new_data/val/' + product + '/' + filename)



# os.mkdir(curDir + '/new_data/test/fresh_banana')