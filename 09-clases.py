class OperasBas:
    #declaracion de propiedades.
    num1 = 0
    num2 = 0    
    res=0
    #declaracion del constructor this
    def __init__(self):
        self.num1=0
        self.num2=0
        #declararcion de metodos de clase

    def suma(self):
        self.res=self.num1+self.num2
        return self.res
    
    def resta(self):
        self.res=self.num1-self.num2
        return self.res

    def main():
        obj=OperasBas()
        obj.suma()
        obj.resta()

#el if _name_ == es para que el proyecto sepa desde que punto iniciara  
if __name__ == "__main__":
    main()  






