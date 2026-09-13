class Sudent_Info:

    def __init__(self,name,subj1,subj2,subj3):
        self.name=name
        self.subj1=subj1
        self.subj2=subj2
        self.subj3=subj3


    def avarg(self):
        result=((self.subj1+self.subj2+self.subj3)/3)
        return result

    @staticmethod
    def print_hello():
        print("I am in print")



s1=Sudent_Info("Ganesh",90,60,80)
s1.print_hello()


