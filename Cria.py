# Escreve no novo ficheiro
def escreve_file(lst_dics):
    file = open("emd.json", mode="w")
    string = "["
    last_dict = 1
    for dict in lst_dics:
        string += "\n\t{"
        last_index = 1
        for index in dict.keys():
            string += "\n\t\t"
            if last_index == len(dict):
                string += '"' + index + '"' + ": " + '"' + str(dict.get(index)) + '"'
            else:
                string += '"' + index + '"' + ": " + '"' + str(dict.get(index)) + '"' + "," 
            last_index += 1
        if last_dict == len(lst_dics):
            string += "\n\t}"
        else:
            string += "\n\t},"
        last_dict += 1        
    string += "\n]"       
    file.write(string)
    file.close()