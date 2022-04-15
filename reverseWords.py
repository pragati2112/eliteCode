from typing import List 


def reverseWords(s: str) -> str:
    sentence = ''
    words = s.split(' ')

    for word in words:
        # print(word[::-1]) use this indexing way to reverse string 


        l=[]
        for w in word:
            l.append(w)

        i=0
        j=len(l)-1

        while i<=j:
            l[i], l[j] = l[j], l[i]
            i+=1
            j-=1     

        for a in l:
            sentence = sentence+a 

        sentence = sentence + ' '  

    return sentence         

           
        



if __name__ == '__main__':
    
    s = "Let's take LeetCode contest "

    print(reverseWords(s))       