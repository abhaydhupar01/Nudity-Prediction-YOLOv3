import os
directory = r"C:\Users\abhay\OneDrive\Desktop\Nudity Prediction\Code files\Vulva_data\final data"

for file in os.listdir(directory):      #1
    if file.endswith('.txt'):
        doc = os.path.join(directory, file)
        with open(doc, "r+") as f:
            lines = f.readlines()
            list_of_lines = []
            for line in lines:
                list_of_lines.append(line)
            
            list_of_newlines = []
            for line in list_of_lines:
                list_line = list(line.split(" "))    
                list_line[0] = "2"
                list_of_newlines.append(list_line)
                f.truncate(0)
                
        with open(doc, "r+") as g:
            for line in list_of_newlines:   
                new_string = ' '.join(map(str, line))
                g.write(new_string)