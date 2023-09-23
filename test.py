str1=input("Enter Any String")
str2=input("Enter a String Which needed to be replaced")
str3=input("New Valie:")
# print(str1[str1.find(str2)])
# print(str1.replace(str1[str1.find(str2)],str3))

# function
def foo(str1:str,str2:str,str3:str)->None:
    print(str1.replace(str1[str1.find(str2)],str3))


# foo(str1,str2,str3)

class BAR(object):

    def __init__(self,str1:str,str2:str,str3:str) -> None:
        self.str1=str1
        self.str2=str2
        self.str3=str3

    def foobar(self)->None:
        print(self.str1.replace(self.str1[str1.find(self.str2)],self.str3))


bar=BAR(str1,str2,str3)
bar.foobar()