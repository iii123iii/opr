from pygame import mixer
from Functions import Functions
class Parser:
    def __init__(self, tokens, UserInput):
        self.tokens = tokens
        self.UserInput = UserInput
        self.ListOfVars = []
        mixer.init()
    
    
    def Parse(self):

        for i , token in enumerate(self.tokens):

            
            #####################################################
            if token == "var" and len(self.tokens) == 4 and self.tokens[2] == "=":
                if self.tokens[i+3][0] == self.tokens[i+3][-1] and self.tokens[i+3][0] in ["'", '"'] or self.tokens[i+3][0] == self.tokens[i+3][-1] and self.tokens[i+3][0] in ["'", '"'] or self.tokens[i+3].isdigit():
                    if self.tokens[i+1][0] == self.tokens[i+1][-1] and self.tokens[i+1][0] in ["'", '"'] or self.tokens[i+3][0] == self.tokens[i+3][-1] and self.tokens[i+1][0] in ["'", '"']:
                        self.Input.ListOfVars.append([self.tokens[1], self.tokens[3]])

            #####################################################
            
            
            
            functions = Functions(self.tokens, token, i)
            
            functions.Print()
            
            functions.Play()
            
            functions.Stop()

            functions.Digit()
            
            functions.Cls()
            
     
                          


             
