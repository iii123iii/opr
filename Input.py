from Lexer import Lexer
import os

os.system("cls")

ListOfVars = []
ListOfTokens = {'print', '+', '-', '*', '/', '(', ')', 'play', 'stop', 'cls', 'var', '=', 'exec'}

##############################################################################################################
from pygame import mixer
from Functions import Functions



class Parser:
    def __init__(self, tokens, UserInput):
        self.tokens = tokens
        self.UserInput = UserInput
        mixer.init()
    
    
    def Parse(self):

        for i , token in enumerate(self.tokens):

            
            #####################################################
            if token == "var" and len(self.tokens) >= 4 and self.tokens[2] == "=":
                if self.tokens[i+3][0] == self.tokens[i+3][-1] and self.tokens[i+3][0] in ["'", '"'] or self.tokens[i+3][0] == self.tokens[i+3][-1] and self.tokens[i+3][0] in ["'", '"'] or self.tokens[i+3].isdigit():
                    if self.tokens[i+1].isalpha() and self.tokens[i+1] not in ListOfTokens and self.tokens[i+1]:
                        VarExists = False
                        for k, var in enumerate(ListOfVars):
                            if(var[0] == self.tokens[i+1]):
                                VarExists = True
                        if(VarExists == False):        
                            ListOfVars.append([self.tokens[1], self.tokens[3]])

            #####################################################
            
            
            functions = Functions(self.tokens, token, i, ListOfVars)
            
            functions.Print()
            
            functions.Play()
            
            functions.Stop()

            functions.Cls()
            
            for j, var in enumerate(ListOfVars):
                if(token == var[0] and len(tokens) == 1):
                    print(var[1][1:-1])
            
            def Exec():
                if token == "exec" and len(self.tokens) == 2:
                    if self.tokens[i+1][0] == "'" and self.tokens[i+1][len(self.tokens[i+1]) - 1] == "'":
                        if(self.tokens[i+1][1:-1][-4:] == ".opm"):
                            print("hello")
                    elif self.tokens[i+1][0] == '"' and self.tokens[i+1][len(self.tokens[i+1]) - 1] == '"':
                        if(self.tokens[i+1][1:-1][-4:] == ".opm"):
                            with open(self.tokens[i+1][1:-1], "r") as file:
                                for line in file:
                                    line = line.rstrip()
                                    Tokens = Lexer(line, ListOfTokens)
                                    tokens = Tokens.ToTokens()
                                    parser = Parser(tokens, line)
                                    parser.Parse()
                    else:
                        S, D = functions.isvar(self.tokens[i+1])
                        if S:
                            print(D[1:-1])
                            
                            
            Exec()                     
            
                
            
##############################################################################################################
            
     
                          


             



while True:
    UserInput = input("Pr > ")
    Tokens = Lexer(UserInput, ListOfTokens)
    tokens = Tokens.ToTokens()
    parser = Parser(tokens, UserInput)
    parser.Parse()
    
    
    
