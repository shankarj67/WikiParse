
import wikipedia
import io
import csv
#create dictionary to store summary and topic
dicti = {}
#open the file with given topic from system
with open('C:\\Users\\SKHK634\\Desktop\\a.txt') as f:
   for line in f:
       try:
        b = wikipedia.summary(line, sentences=1)                        
       # file = open('C:\\Users\\SKHK634\\Desktop\\output.txt', 'w')
        dicti.update({line:b})                                                    
        if 'str' in line:
              break         
       except:
          pass
   
#clean the unnecessary character from dictionary
clean_dict = {key.strip(): item.strip() for key, item in dicti.items()}

#to remove the encoding/decoding error
encoding = 'utf-16le' #for window user
# Try this if above code will not work encoding = 'utf-8'


#save as notepad(text file)      
with io.open('C:\\Users\\SKHK634\\Desktop\\output.txt','w', encoding=encoding) as f:
      for key, value in clean_dict.items():
        f.write('%s:: %s\n' % (key, value))
        f.write('\n')
   
#save as csv
with open('C:\\Users\\SKHK634\\Desktop\\output.csv', 'w',encoding=encoding) as csv_file:
    writer = csv.writer(csv_file)
    for key, value in clean_dict.items():
       writer.writerow([key, value])



#print the summary of any topic using key
print(clean_dict['google'])  #choose any key to print desired value 
