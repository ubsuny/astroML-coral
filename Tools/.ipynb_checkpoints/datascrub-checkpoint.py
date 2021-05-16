import csv


##########################################################################################
#                                                                                        #
#    Function: datapull()                                                                #
#    Inputs: string name of .txt file with .fits locations, string name of output .csv   #
#    Return: none, creates a .csv with Kepler IDs, urls for .fits file at MAST archive   #
#    Notes: Requires manual conversion of MAST bulk download scripts to .txt files.      #
#                                                                                        #  
##########################################################################################
def datapull(input, output):
    con1 = isinstance(input, str)
    con2 = isinstance(output, str)
    
    if con1 == True and con2 == True:
        lines = []
        system = []
        url = []
        
        with open(input) as f:
            for dat in f:
                line = dat[100:]
                sys = line[:9]
                sys = int(sys)
                sys = str(sys)
                urls = line[35:]
                lines.append(line)
                system.append(sys)
                url.append(urls)
                
        f.close()
        
        url = [i.replace("'\n", '') for i in url]
        data = zip(system, url)
        data = list(data)
        header = ['KepID', 'URL']
        
        
        with open(output, 'w', newline='') as d:
            writer = csv.writer(d, quoting=csv.QUOTE_ALL)
            writer.writerow(header)
            writer.writerows(data)
        d.close()
        print("Successfuly pulled system data from: " , input)
    else:
        print('Error: Please enter strings with input .txt file and output .csv file')
        
        
        

###########################################################################################################
#                                                                                                         #                                                                    
#    Function: various   (used only internally so not important)                                          #                                               
#    Inputs: something                                                                                    #  
#    Return: yes                                                                                          #   
#    Notes: *Trio of functions for converting the exoplanet designations from strings to ints             # 
#           *Yeah, spaghetti but it works. Don't ask how                                                  #  
#           *REQUIRES cumulative.csv TO BE PRESENT IN REPO (kepler pipeline data saved locally as .csv)   #   
###########################################################################################################
def cleaner(data):
    des = ['CONFIRMED', 'CANDIDATE', 'FALSE POSITIVE']
    for i in data:
        if i[1] == des[0]:
            i[1] = 1
        elif i[1] == des[2]:
            i[1] = 3
        elif i[1] == des[1]:
            i[1] = 2
    return data   

def converter(data):
    t = cleaner(data)
    u = cleaner(t)
    v = cleaner(u)
    w = cleaner(v)
    x = cleaner(w)
    y = cleaner(x)
    z = cleaner(y)
    return z

def exo_num_des():
    system = []
    status = []
    
    with open('cumulative.csv', 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            system.append(row[1])
            status.append(row[4])
        print(type(system))
        data = zip(system, status)
        data = list(data)
        data = [list(i) for i in data]
    data = converter(data)
    with open("fix_exo_dat.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print('Kepler pipeline data converted')    

    
    
    
    
##########################################################################################
#                                                                                        #
#    Function: exomatch()                                                                #
#    Inputs: dataset1, dataset 2                                                         #
#    Return: elements of dataset1 present in dataset2                                    #
#    Notes: Simple search function, used only internally                                 #
#                                                                                        #  
##########################################################################################    
    
    
def exomatch(data, actual):
    exoplanets = [] 
    for i in data:
        for j in actual:
            if i == j:
                exoplanets.append(i)  
    return exoplanets




##########################################################################################
#                                                                                        #
#    Function: exofinder()                                                               #
#    Inputs: input .txt file, output .csv file, Bool for return                          #
#    Return:  (optional), gives list of systems with suspected or confirmed exoplanets   #
#    Notes: Magic spaghetti.  Parse at your own risk                                     #
#                                                                                        #
#                                                                                        #  
##########################################################################################
def exofinder(infile, outfile, exoIDs):
    con1 = isinstance(infile, str)
    con2 = isinstance(outfile, str)
    if con1 == True and con2 == True:
        exo_num_des()

        sys_act = []
        status = []
        with open('fix_exo_dat.csv', 'r') as f:
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                sys_act.append(row[0])
                status.append(row[1])
        sys2 = []
        url = []

        datapull(infile, outfile)
        with open(outfile, 'r') as f:
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                sys2.append(row[0])
                url.append(row[1])

        dat = exomatch(sys2, sys_act)
       
       
        data = zip(sys2, url)
        data = [list(ele) for ele in data]
        act = zip(sys_act, status)
        act = [list(ele) for ele in act]

       
        for i in range(len(sys2)):
            for x in range(len(sys_act)):
                if sys2[i] == sys_act[x]:
                    data[i].append(int(act[x][1]))
        data[0].append('Status')
        for i in data:
            if len(i) == 2:
                i.append(0)
            i[:] = i[0:3]
                
        with open(outfile, 'w', newline='') as d:
            writer = csv.writer(d, quoting=csv.QUOTE_ALL)
            writer.writerows(data)
        d.close()
        if exoIDs == True:
            return dat
        
    else:
        print('Error: Please enter strings with input .txt file and output .csv file')