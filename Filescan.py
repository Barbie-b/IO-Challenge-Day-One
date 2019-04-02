
file=open("justo.txt","r")#variable name for the opened file 

#function to count number of lines in the text file
def num_line():
    count=0
    for line in file:
        count+=1

    print(count)

#function to count number of words in the text file
def num_words():
    num=0
    line=0
    word=''
    
    for line in file:
        for word in line:
            num+=1

    print(num)
        
#function to return all words  in the text file
def ret_words():
    line=0
    for line in file:
        for word in line:
            print(word)

#function to count number of vowels in the text file
def num_vowels():
    line=0
    temp=0
    vowel=0
   
    for line in file:
        
        for word in line:
            
            for letter in word:
                if (letter=='A' or letter=='a'):
                    vowel=vowel+1
                if (letter=='E' or letter=='e'):
                    vowel=vowel+1

                if (letter=='I' or letter=='i'):
                    vowel=vowel+1

                if (letter=='o' or letter=='o'):
                    vowel=vowel+1

                if (letter=='U' or letter=='u'):
                    vowel=vowel+1

    print(vowel)

#function to count frequency of each character in the text file 
def freq_char():
    all_freq={}
    
    for line in file:
        for word in line:
            
            for letter in word:
                if letter in all_freq:
                    all_freq[letter] +=1
                else:
                    all_freq[letter]=1

    print("count of all all characters:"+str(all_freq))
                
                
   


#print(freq_char())
    
#print(ret_words())

#num_line()            
            
num_words()

num_line()  

#print(num_vowels())
      







file.close()
