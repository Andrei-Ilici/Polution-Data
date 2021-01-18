
def create_single_list(elem,number):
    current_list = []
    
    for i in range (1, len(elem)):
        current_list.append(elem[i][number])
        
    return current_list

def create_complete_list(filename, lines):
    big_list = []
    
    for j in range(len(lines[2])):
        big_list.append(create_single_list(lines,j))
        
    return big_list