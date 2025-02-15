Task1.py
def kwargsAcceptFun(**a):
    print("Named arguments:")
    for key, val in a.items():
        print(key,":",val)

#Call    
kwargsAcceptFun(Name="Feruza Jo'rayeva", Age=20, Study="NUU", Major="Economics and Data Science", Hobby="Reading", Country="Uzbekistan")
   
    
