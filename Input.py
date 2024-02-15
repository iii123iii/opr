from Lexer import Lexer
import os
import platform

if platform == "linux" or platform == "linux2":
    os.system("clear")
elif platform == "win32":
  os.system("cls")


ListOfVars = []
ListOfTokens = {'print', '+', '-', '*', '/', '(', ')', 'play', 'stop', 'cls', 'var', '=', 'exec', 'exit'}

##############################################################################################################
import contextlib
import os

with contextlib.redirect_stdout(open(os.devnull, 'w')):
    from pygame import mixer
from Functions import Functions



class Parser:
    def __init__(self, tokens, UserInput):
        self.tokens = tokens
        self.UserInput = UserInput
        self.OnFile = False
        mixer.init()
    
    
    def Parse(self):

        for i , token in enumerate(self.tokens):

            
            #####################################################
            
            if token == "var" and len(self.tokens) >= 4 and self.tokens[2] == "=":
                if self.tokens[i+3][0] == self.tokens[i+3][-1] and self.tokens[i+3][0] in ["'", '"'] or self.tokens[i+3][0] == self.tokens[i+3][-1] and self.tokens[i+3][0] in ["'", '"'] or self.tokens[i+3].replace(".", "", 1).isdigit():
                    if self.tokens[i+1].isalpha() and self.tokens[i+1] not in ListOfTokens and self.tokens[i+1]:
                        VarExists = False
                        for k, var in enumerate(ListOfVars):
                            if(var[0] == self.tokens[i+1]):
                                VarExists = True
                        if(VarExists == False):        
                            ListOfVars.append([self.tokens[1], self.tokens[3]])
                            
            def Exec():
                if token == "exec" and len(self.tokens) == 2:
                    if self.tokens[i+1][0] == "'" and self.tokens[i+1][len(self.tokens[i+1]) - 1] == "'":
                        if(self.tokens[i+1][1:-1][-4:] == ".opm"):
                            with open(self.tokens[i+1][1:-1], "r") as file:
                                for line in file:
                                    self.OnFile = True
                                    line = line.rstrip()
                                    Tokens = Lexer(line, ListOfTokens)
                                    tokens = Tokens.ToTokens()
                                    parser = Parser(tokens, line)
                                    parser.Parse()
                                self.OnFile = False  
                    elif self.tokens[i+1][0] == '"' and self.tokens[i+1][len(self.tokens[i+1]) - 1] == '"':
                        if(self.tokens[i+1][1:-1][-4:] == ".opm"):
                               with open(self.tokens[i+1][1:-1], "r") as file:
                                for line in file:
                                    self.OnFile = True
                                    line = line.rstrip()
                                    Tokens = Lexer(line, ListOfTokens)
                                    tokens = Tokens.ToTokens()
                                    parser = Parser(tokens, line)
                                    parser.Parse()
                                self.OnFile = False    
                    else:
                        S, D = functions.isvar(self.tokens[i+1])
                        if S:
                            if(D[1:-1][-4:] == ".opm"):
                                    with open(D[1:-1], "r") as file:
                                        for line in file:
                                            self.OnFile = True
                                            line = line.rstrip()
                                            Tokens = Lexer(line, ListOfTokens)
                                            tokens = Tokens.ToTokens()
                                            parser = Parser(tokens, line)
                                            parser.Parse()
                                        self.OnFile = False                  

            #####################################################
            
            
            functions = Functions(self.tokens, token, i, ListOfVars)
            
            functions.Print()
            
            functions.Play()
            
            functions.Stop()

            functions.Cls()
            
            functions.Exit()                        
                            
            Exec()
            
            for j, var in enumerate(ListOfVars):
                if(token == var[0] and len(tokens) == 1):
                    print(var[1][1:-1])
            
            
            if(token[1:-1].replace(".", "", 1).replace("-", "", 1).isdigit() and len(tokens) == 1):
                print(token[1:-1])
            
            if i == 0 and len(self.tokens) == 3 and self.tokens[1] == "=" and self.tokens[2][0] == self.tokens[2][-1] and self.tokens[2][0] in ["'", '"']:
                target = None
                for i, v in enumerate(ListOfVars):
                    if v[0] == self.tokens[0]:
                        target = i
                if target != None:
                    ListOfVars[target] = [self.tokens[0], self.tokens[2]]
            else:
                if i == 0 and len(self.tokens) == 3:
                    S, D = functions.isvar(self.tokens[2])
                    if S:
                        if self.tokens[1] == "=" and D[0] == D[-1] and D[0] in ["'", '"']:
                            target = None
                            for i, v in enumerate(ListOfVars):
                                if v[0] == self.tokens[0]:
                                    target = i
                            if target != None:
                                ListOfVars[target] = [self.tokens[0], D]
            
                
            
##############################################################################################################
            
     
                          


             



while True:
    UserInput = input("Opr > ")
    Tokens = Lexer(UserInput, ListOfTokens)
    tokens = Tokens.ToTokens()
    parser = Parser(tokens, UserInput)
    parser.Parse()
    
    
    
