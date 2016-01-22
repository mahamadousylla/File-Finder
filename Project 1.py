#Mahamadou Sylla 61549479 and Yilin Zhu 93638450 for Project 1


from pathlib import Path
import os
import shutil


def check_if_valid_path():

    result = False
    
    while result == False: # always

        input_one = input()

        result = Path(input_one).exists() # if this is true do what?

        if result == True:
            return input_one
            break
        
        print('ERROR')

def check_if_valid_search():

    result = False

    search = 'NE'
    
    while result == False: # always

        input_two = input()


        if input_two.split()[0] == 'S' and input_two.split()[-1].isnumeric(): # if this is true do what?
            result = True

        else:
            result = input_two.split()[0] in search

        
        if result == True:
            return input_two
            break
        
        print('ERROR')

def check_if_valid_action():

    result = False

    search = 'PFDT'
    
    while result == False: # always

        input_three = input()

        result = input_three in search # if this is true do what?

        if result == True:
            return input_three
            break
        
        print('ERROR')

    


def LookthroughAllDirectory(input_one):
    '''
    looks through the main directory and all
    its subdirectories for different files, and does
    something interesting on the files
    '''

    ListofDirectory = [ ] #empty list
    
    try:
        
        for obj in Path(input_one).iterdir(): #for every object in this directory
            

            if obj.is_file(): #if object is a file, do this
                ListofDirectory.append(obj) #append file to ListofDirectory
                

            elif obj.is_dir(): #if object is not a file, do this 
                ListofDirectory.extend(LookthroughAllDirectory(obj)) #recursion

    
        return ListofDirectory

    except FileNotFoundError:

        print('ERROR')


def search_characteristics(input_two) -> list:          

    try:
        

        List = [ ]


        if input_two.startswith('N'): #if line starts with N

            newLine = input_two.split()[-1] #split the line and grab the file to be searched for

            new = LookthroughAllDirectory(input_one) #recursive function

            for item in new: #for every path in the recursive function list

                str_item = str(item) #convert path to a string 

                if str_item.endswith(newLine): #if string version of path ends with what user searched for

                    List.append(item) #add the path to the list

                        

        elif input_two.startswith('E'): #if line starts with E

            newLine = input_two.split()[-1] #split the line and grab file extension to be searched for

            new = LookthroughAllDirectory(input_one) #recursive function
 
            for item in new: #for every path in recursive function list

                str_item = str(item) #convert path to a string

                name, extension = os.path.splitext(str_item) #split the filname and extension

                if extension.strip('.') == newLine or extension == newLine: #if extension ends with what user searched for

                    List.append(item) #add this item to List
                     

        elif input_two.startswith('S'): #if line starts with S

            newLine = input_two.split()[-1] #split the line and grab what size of file should be searched for

            new = LookthroughAllDirectory(input_one) #recursive function

            for item in new: #for every item in recursive function list

                str_item = str(item) #convert path to a string

                size = os.path.getsize(str_item) #get size of each file in bytes

                if size > int(newLine): #if size of each file in bytes is greater than what the user inputted

                    List.append(item) #add this item to List
                    

        return List
        
    except:

        print('ERROR')


def something_interesting(input_three):
    
    try:


        if input_three == 'P': #if input is P

            result = search_characteristics(input_two) #run search characteristics, which gives us a list

            for path in result: #for each path in result

                print(path) #print path to console


        elif input_three == 'F': #if input is F

            result = search_characteristics(input_two) #run search characteristics, which gives us a list

            for path in result: #for each path in result
                
                print(path) #print path to console
                
                str_item = str(path) #convert path to a string
                
                p = Path(str_item) #store path(str_item) into variable p
                
                with p.open() as file: #open file
                    f = file.readline() #reads first line of file
                    print(f) #prints first line of file to console


        elif input_three == 'D': #if input is D

            result = search_characteristics(input_two) #run search characteristics, which gives us a list

            for path in result:

                new_path = str(path)

                print(path)

                f2 = new_path + '.dup'

                shutil.copy(new_path, f2)
            


        elif input_three == 'T': #if input is T

            result = search_characteristics(input_two) #run search characteristics, which gives us a list

            for path in result:
                
                str_name = str(path) #convert path to a string

                print(path) #print path to console
                
                os.utime(str_name) #modify timestamp
               

            
    except UnicodeDecodeError:
        print('ERROR')

input_one = check_if_valid_path()
input_two = check_if_valid_search()
input_three = check_if_valid_action()

def run_program():
    LookthroughAllDirectory(input_one)
    search_characteristics(input_two)
    something_interesting(input_three)


            
if __name__ == '__main__':
    run_program()
