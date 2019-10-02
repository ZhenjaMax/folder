import wikipedia                                                                
                                                                                
pages_list = str(input())                                                       
pages_list = pages_list.split(', ')                                             
                                                                                
if pages_list[-1] in wikipedia.languages():                                     
    wikipedia.set_lang(pages_list[-1])                                          
    del pages_list[-1]                                                          
else:                                                                           
    print('no results')                                                         
    exit()                                                                      
                                                                                
from help_wiki_function import is_page_valid                                    
for i in pages_list:                                                            
    if not is_page_valid(i):                                                    
        pages_list.remove(i)                                                    
                                                                                
max_words, page_number_max = 0, 0                                               
for i in range(len(pages_list)):                                                
    text = wikipedia.summary(pages_list[i])                                     
    words = text.count(' ') + 1                                                 
    if words >= max_words:                                                      
        max_words = words                                                       
        page_number_max = i                                                     
print(max_words, wikipedia.page(pages_list[page_number_max]).title)          

# -------------------------------OK-------------------------------------------

chain=[]                                                     
chain.append(pages_list[0])                                                     
for i in range(len(pages_list)-1):
    links=wikipedia.page(pages_list[i]).links
    if pages_list[i+1] in links:
        chain.append(pages_list[i+1])                                           
    else:
        for j in range(len(links))
            sublinks=wikipedia.page(links[j]).links                                                                                
            if pages_list[i+1] in sublinks:                      
                chain.append()                                                 
                chain.append(pages_list[i+1])
                continue                                 
print(chain)
